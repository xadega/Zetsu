from config import LOG, LOG_GROUP_ID
from zetsu import app
from zetsu.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "**ɢꝛᴏᴜᴘ ᴘꝛɪʙᴀᴅɪ**"
        logger_text = f"""
🤖 **ᴢɛᴛꜱᴜ ʟᴏɢɢᴇꝛ**
────────────────────────
• **ɢꝛᴏᴜᴘ** -≽ {message.chat.title} | `{message.chat.id}`
• **ʟɪɴᴋ ɢꝛᴏᴜᴘ** -≽ {chatusername}
• **ɴᴀᴍᴀ** -≽ {message.from_user.mention}
• **ɪᴅ ᴘɛɴɢɢᴜɴᴀ** -≽ `{message.from_user.id}`
• **ɴᴀᴍᴀ ᴘɛɴɢɢᴜɴᴀ** -≽ @{message.from_user.username}
────────────────────────
• **ᴘɛɴᴄᴀꝛɪᴀɴ** -≽ {message.text}
• **sᴛꝛɛᴀᴍɪɴɢ** -≽ {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
