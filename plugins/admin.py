# (c) @AbirHasan2005

import traceback
import os

from database import Database
from pyrogram import Client, filters

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

db = Database(Config.DATABASE_URL, Config.SESSION_NAME)
CURRENT_PROCESSES = {}
CHAT_FLOOD = {}
broadcast_ids = {}


@Client.on_message(filters.command('total'))
async def sts(c, m):
    if m.from_user.id != Config.OWNER_ID:
        return 
    total_users = await db.total_users_count()
    await m.reply_text(text=f"Toplam kullanıcı(lar) {total_users}", quote=True)


@Client.on_message(filters.command('ban'))
async def ban(c, m):
    if m.from_user.id != Config.OWNER_ID:
        return
    if len(m.command) == 1:
        await m.reply_text(
            f"Herhangi bir kullanıcıyı bottan yasaklamak için bu komutu kullanın.\n\nKullanım:\n\n`/ban_user user_id ban_duration ban_reason`",
            quote=True
        )
        return
    
    try:
        user_id = int(m.command[1])
        ban_duration = int(m.command[2])
        ban_reason = ' '.join(m.command[3:])
        ban_log_text = f"{user_id} kullanıcısı {ban_reason} nedeniyle {ban_duration} gün süreyle yasaklandı."
        
        try:
            await c.send_message(
                user_id,
                f"Bu botta yasaklandınız **{ban_duration}** gün\nsebep __{ban_reason}__ \n\n**yöneticiden mesaj**"
            )
            ban_log_text += '\n\nKullanıcı başarıyla bilgilendirildi!'
        except:
            traceback.print_exc()
            ban_log_text += f"\n\nKullanıcı bildirimi başarısız oldu! \n\n`{traceback.format_exc()}`"
        await db.ban_user(user_id, ban_duration, ban_reason)
        print(ban_log_text)
        await m.reply_text(
            ban_log_text,
            quote=True
        )
    except:
        traceback.print_exc()
        await m.reply_text(
            f"Hata oluştu! Aşağıda verilen geri izleme\n\n`{traceback.format_exc()}`",
            quote=True
        )


@Client.on_message(filters.command('unban'))
async def unban(c, m):
    if m.from_user.id != Config.OWNER_ID:
        return
    if len(m.command) == 1:
        await m.reply_text(
            f"Herhangi bir kullanıcının yasağını kaldırmak için bu komutu kullanın.\n\nKullanım:\n\n`/unban_user user_id`",
            quote=True
        )
        return
    
    try:
        user_id = int(m.command[1])
        unban_log_text = f"Kullanıcı yasağı kaldırılıyor {user_id}"
        
        try:
            await c.send_message(
                user_id,
                f"Yasağınız kaldırıldı!"
            )
            unban_log_text += '\n\nKullanıcı başarıyla bilgilendirildi!'
        except:
            traceback.print_exc()
            unban_log_text += f"\n\nKullanıcı bildirimi başarısız oldu! \n\n`{traceback.format_exc()}`"
        await db.remove_ban(user_id)
        print(unban_log_text)
        await m.reply_text(
            unban_log_text,
            quote=True
        )
    except:
        traceback.print_exc()
        await m.reply_text(
            f"Hata oluştu! Aşağıda verilen geri izleme\n\n`{traceback.format_exc()}`",
            quote=True
        )


@Client.on_message(filters.command('banned_users'))
async def _banned_usrs(c, m):
    if m.from_user.id != Config.OWNER_ID:
        return
    all_banned_users = await db.get_all_banned_users()
    banned_usr_count = 0
    text = ''
    async for banned_user in all_banned_users:
        user_id = banned_user['id']
        ban_duration = banned_user['ban_status']['ban_duration']
        banned_on = banned_user['ban_status']['banned_on']
        ban_reason = banned_user['ban_status']['ban_reason']
        banned_usr_count += 1
        text += f"> **user_id**: `{user_id}`, **Ban Süresi**: `{ban_duration}`, **Yasaklı**: `{banned_on}`, **Sebep**: `{ban_reason}`\n\n"
    reply_text = f"Toplam yasaklı kullanıcı(lar): `{banned_usr_count}`\n\n{text}"
    if len(reply_text) > 4096:
        with open('banned-users.txt', 'w') as f:
            f.write(reply_text)
        await m.reply_document('banned-users.txt', True)
        os.remove('banned-users.txt')
        return
    await m.reply_text(reply_text, True)
