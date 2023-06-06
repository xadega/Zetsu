from pyrogram import filters
from pyrogram.types import Message

from strings import get_command
from zetsu import app
from zetsu.misc import SUDOERS
from zetsu.utils.database.memorydatabase import (
    get_active_chats, get_active_video_chats)
from zetsu import userbot

# Commands
ACTIVEVC_COMMAND = get_command("ACTIVEVC_COMMAND")
ACTIVEVIDEO_COMMAND = get_command("ACTIVEVIDEO_COMMAND")


@app.on_message(filters.command(ACTIVEVC_COMMAND, [".", "(", "-", "!", "/"]) & SUDOERS)
async def activevc(_, message: Message):
    mystic = await message.reply_text(
        "**Fetching...**"
    )
    served_chats = await get_active_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except Exception:
            title = "Grup Privat"
        if (await app.get_chat(x)).username:
            user = (await app.get_chat(x)).username
            text += f"<b>{j + 1}.</b> [{title}](https://t.me/{user}) | `{x}`\n"
        else:
            text += f"<b>{j + 1}. {title}</b> | `{x}`\n"
        j += 1
    if not text:
        await mystic.edit_text("❎ **Not Available...**")
    else:
        await mystic.edit_text(
            f"🎧 **Chats Music Active**\n{text}",
            disable_web_page_preview=True,
        )


@app.on_message(filters.command(ACTIVEVIDEO_COMMAND, [".", "(", "-", "!", "/"]) & SUDOERS)
async def activevi_(_, message: Message):
    mystic = await message.reply_text(
        "**Fetching...**"
    )
    served_chats = await get_active_video_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except Exception:
            title = "Grup Privat"
        if (await app.get_chat(x)).username:
            user = (await app.get_chat(x)).username
            text += f"<b>{j + 1}.</b> [{title}](https://t.me/{user}) | `{x}`\n"
        else:
            text += f"<b>{j + 1}. {title}</b> | `{x}`\n"
        j += 1
    if not text:
        await mystic.edit_text("❎ **Not Available...**")
    else:
        await mystic.edit_text(
            f"🎥 **Chats Stream Active**\n{text}",
            disable_web_page_preview=True,
        )


@app.on_message(filters.command("active", [".", "(", "-", "!", "/"]) & SUDOERS)
async def activezetsu(_, message: Message):
    vc = len(await get_active_chats())
    vd = len(await get_active_video_chats())
    await app.send_message(message.chat.id, 
        f"💽 **Chats Active**\n× **Music** » **{vc}**\n× **Stream** » **{vd}**")


@app.on_message(filters.command("ass", [".", "(", "-", "!", "/"]) & SUDOERS)
async def asszetsu(_, message: Message):
    await userbot.one.send_message(message.chat.id, "**Hadir Adam Sayang** 😍")
    await userbot.two.send_message(message.chat.id, "**Hadir dong Adam Ganteng** 😝")
    await userbot.three.send_message(message.chat.id, "**Hadir Tuanku Dam** 🤩")
    await userbot.four.send_message(message.chat.id, "**Hadir Adam** 😘")
    await userbot.five.send_message(message.chat.id, "**Hadir Dam** 👋")
