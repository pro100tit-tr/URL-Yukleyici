import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

from plugins.yt_dlp_button import yt_dlp_call_back
from plugins.dl_button import ddl_call_back
from translation import Translation
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_callback_query()
async def button(bot, update):
    cb_data = update.data
    if "|" in cb_data:
        await yt_dlp_call_back(bot, update)
    elif "=" in cb_data:
        await ddl_call_back(bot, update)
    elif cb_data == "help":
        await update.message.edit_text(
            text=Translation.HELP_TEXT,
            disable_web_page_preview=True
        )
    elif cb_data == "close":
        await update.message.delete()
