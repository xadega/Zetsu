from pyrogram import filters

import config
from strings import get_command
from zetsu import app
from config import OWNER_ID
from zetsu.utils.database import autoend_off, autoend_on
from zetsu.utils.decorators.language import language

# Commands
AUTOEND_COMMAND = get_command("AUTOEND_COMMAND")


@app.on_message(filters.command(AUTOEND_COMMAND, [".", "^", "-", "!", "/"]) & filters.user(OWNER_ID))
async def auto_end_stream(client, message):
    usage = "**Penggunaan:**\n\n/autoend on | off"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "on":
        await autoend_on()
        await message.reply_text(
            "✅ `Auto End Stream Diaktifkan...`"
        )
    elif state == "off":
        await autoend_off()
        await message.reply_text("✅ `Auto End Stream Dimatikan...`")
    else:
        await message.reply_text(usage)
