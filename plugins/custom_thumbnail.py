#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import numpy
import os
from PIL import Image
import time
import pyrogram
from pyrogram import Client, filters
from translation import Translation

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@Client.on_message(filters.command(["genthumb"]))
async def generate_custom_thumbnail(c, m):
    if m.reply_to_message is not None:
        reply_message = m.reply_to_message
        if reply_message.media_group_id is not None:
            download_location = Config.DOWNLOAD_LOCATION + "/" + str(m.from_user.id) + "/" + str(reply_message.media_group_id) + "/"
            save_final_image = download_location + str(round(time.time())) + ".jpg"
            list_im = os.listdir(download_location)
            if len(list_im) == 2:
                imgs = [ Image.open(download_location + i) for i in list_im ]
                inm_aesph = sorted([(numpy.sum(i.size), i.size) for i in imgs])
                min_shape = inm_aesph[1][1]
                imgs_comb = numpy.hstack(numpy.asarray(i.resize(min_shape)) for i in imgs)
                imgs_comb = Image.fromarray(imgs_comb)
                # combine: https://stackoverflow.com/a/30228789/4723940
                imgs_comb.save(save_final_image)
                # send
                user = await bot.get_me()
                mention = user["mention"]
                await c.send_photo(
                    chat_id=m.chat.id,
                    photo=save_final_image,
                    caption=Translation.CUSTOM_CAPTION_UL_FILE.format(mention),
                    reply_to_message_id=m.message_id
                )
            else:
                await c.send_message(
                    chat_id=m.chat.id,
                    text=Translation.ERR_ONLY_TWO_MEDIA_IN_ALBUM,
                    reply_to_message_id=m.message_id
                )
            try:
                [os.remove(download_location + i) for i in list_im ]
                os.remove(download_location)
            except:
                pass
        else:
            await c.send_message(
                chat_id=m.chat.id,
                text=Translation.REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB,
                reply_to_message_id=m.message_id
            )
    else:
        await c.send_message(
            chat_id=m.chat.id,
            text=Translation.REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB,
            reply_to_message_id=m.message_id
        )


@Client.on_message(filters.private & filters.photo)
async def save_photo(c, m):
    v = await m.reply_text("Thumbnail Kaydediliyor.", True)
    if m.media_group_id is not None:
        # album is sent
        download_location = Config.DOWNLOAD_LOCATION + "/" + str(m.from_user.id) + "/" + str(m.media_group_id) + "/"
        if not os.path.isdir(download_location):
            os.mkdir(download_location)
        await c.download_media(
            message=m,
            file_name=download_location
        )
    else:
        # received single photo
        download_location = Config.DOWNLOAD_LOCATION + "/" + str(m.from_user.id) + ".jpg"
        await c.download_media(
            message=m,
            file_name=download_location
        )
        try:
           await v.edit_text("Thumbnail Kaydedildi.")
        except Exception as e:
          log.info(f"#Hata {e}")
        
@Client.on_message(filters.command(["delthumb"]))
async def delete_thumbnail(c,m):
    download_location = Config.DOWNLOAD_LOCATION + "/" + "thumbnails" + "/" + str(m.from_user.id)
    try:
        os.remove(download_location + ".jpg")
    except:
        pass
    await m.reply_text("Thumbnail Kaldırıldı.",quote=True)
