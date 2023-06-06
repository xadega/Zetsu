from pyrogram import filters

import config
from config import OWNER_ID
from strings import get_command
from zetsu import app
from zetsu.utils.database import add_off, add_on
from zetsu.utils.decorators.language import language

# Commands
LOGGER_COMMAND = get_command("LOGGER_COMMAND")


@app.on_message(filters.command(LOGGER_COMMAND, [".", "^", "-", "!", "/"]) & filters.user(OWNER_ID))
@language
async def logger(client, message, _):
    usage = _["log_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "on":
        await add_on(config.LOG)
        await message.reply_text(_["log_2"])
    elif state == "off":
        await add_off(config.LOG)
        await message.reply_text(_["log_3"])
    else:
        await message.reply_text(usage)
