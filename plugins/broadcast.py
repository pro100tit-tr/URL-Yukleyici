# (c) @AbirHasan2005 | X-Noid

import traceback, datetime, asyncio, string, random, time, os, aiofiles, aiofiles.os
from database import Database
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

db = Database(Config.DATABASE_URL, Config.SESSION_NAME)
CURRENT_PROCESSES = {}
CHAT_FLOOD = {}
broadcast_ids = {}

async def send_msg(user_id, message):
    try:
        await message.copy(chat_id=user_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return send_msg(user_id, message)
    except InputUserDeactivated:
        return 400, f"{user_id} : devre dışı\n"
    except UserIsBlocked:
        return 400, f"{user_id} : botu engelledi\n"
    except PeerIdInvalid:
        return 400, f"{user_id} : kullanıcı kimliği geçersiz\n"
    except Exception as e:
        return 500, f"{user_id} : {traceback.format_exc()}\n"
        

@Client.on_message(filters.command('broadcast') & filters.reply)
async def broadcast_(c, m):
    if m.from_user.id != Config.OWNER_ID:
        return
    all_users = await db.get_all_users()
    
    broadcast_msg = m.reply_to_message
    
    while True:
        broadcast_id = ''.join([random.choice(string.ascii_letters) for i in range(3)])
        if not broadcast_ids.get(broadcast_id):
            break
    
    out = await m.reply_text(
        text = f"Yayın başladı! Tüm kullanıcılar bilgilendirildiğinde günlük dosyası ile bilgilendirileceksiniz."
    )
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    failed = 0
    success = 0
    
    broadcast_ids[broadcast_id] = dict(
        total = total_users,
        current = done,
        failed = failed,
        success = success
    )
    
    async with aiofiles.open('broadcast.txt', 'w') as broadcast_log_file:
        async for user in all_users:
            
            sts, msg = await send_msg(
                user_id = int(user['id']),
                message = broadcast_msg
            )
            if msg is not None:
                await broadcast_log_file.write(msg)
            
            if sts == 200:
                success += 1
            else:
                failed += 1
            
            if sts == 400:
                await db.delete_user(user['id'])
            
            done += 1
            if broadcast_ids.get(broadcast_id) is None:
                break
            else:
                broadcast_ids[broadcast_id].update(
                    dict(
                        current = done,
                        failed = failed,
                        success = success
                    )
                )
    if broadcast_ids.get(broadcast_id):
        broadcast_ids.pop(broadcast_id)
    completed_in = datetime.timedelta(seconds=int(time.time()-start_time))
    
    await asyncio.sleep(3)
    
    await out.delete()
    
    if failed == 0:
        await m.reply_text(
            text=f"Yayın tamamlandı `{completed_in}`\n\nToplam kullanıcı {total_users}.\nToplam yapılan {done}, {success} başarılı {failed} başarısız.",
            quote=True
        )
    else:
        await m.reply_document(
            document='broadcast.txt',
            caption=f"Yayın `{completed_in}` içinde tamamlandı\n\nToplam kullanıcı {total_users}.\nToplam yapılan yayın {done}, {success} başarılı {failed} başarısız.",
            quote=True
        )
    
    await aiofiles.os.remove('broadcast.txt')
