import asyncio

from pyrogram import filters

import config
from strings import get_command
from zetsu import app
from config import OWNER_ID
from zetsu.utils.database.memorydatabase import get_video_limit
from zetsu.utils.formatters import convert_bytes

VARS_COMMAND = get_command("VARS_COMMAND")


@app.on_message(filters.command(VARS_COMMAND, [".", "^", "-", "!", "/"]) & filters.user(OWNER_ID))
async def varsFunc(client, message):
    mystic = await message.reply_text(
        "ℹ️ **Mohon Tunggu...**"
    )
    v_limit = await get_video_limit()
    bot_name = config.MUSIC_BOT_NAME
    up_r = f"[Repo]({config.UPSTREAM_REPO})"
    up_b = config.UPSTREAM_BRANCH
    auto_leave = config.AUTO_LEAVE_ASSISTANT_TIME
    yt_sleep = config.YOUTUBE_DOWNLOAD_EDIT_SLEEP
    tg_sleep = config.TELEGRAM_DOWNLOAD_EDIT_SLEEP
    playlist_limit = config.SERVER_PLAYLIST_LIMIT
    fetch_playlist = config.PLAYLIST_FETCH_LIMIT
    song = config.SONG_DOWNLOAD_DURATION
    play_duration = config.DURATION_LIMIT_MIN
    cm = config.CLEANMODE_DELETE_MINS
    auto_sug = config.AUTO_SUGGESTION_TIME
    if config.AUTO_LEAVING_ASSISTANT == str(True):
        ass = "Yes"
    else:
        ass = "No"
    if config.PRIVATE_BOT_MODE == str(True):
        pvt = "Yes"
    else:
        pvt = "No"
    if config.AUTO_SUGGESTION_MODE == str(True):
        a_sug = "Yes"
    else:
        a_sug = "No"
    if config.AUTO_DOWNLOADS_CLEAR == str(True):
        down = "Yes"
    else:
        down = "No"

    if not config.GITHUB_REPO:
        git = "No"
    else:
        git = f"[Repo]({config.GITHUB_REPO})"
    if not config.START_IMG_URL:
        start = "No"
    else:
        start = f"[Image]({config.START_IMG_URL})"
    if not config.SUPPORT_CHANNEL:
        s_c = "No"
    else:
        s_c = f"[Channel]({config.SUPPORT_CHANNEL})"
    if not config.SUPPORT_GROUP:
        s_g = "No"
    else:
        s_g = f"[Group]({config.SUPPORT_GROUP})"
    if not config.GIT_TOKEN:
        token = "No"
    else:
        token = "Yes"
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        sotify = "No"
    else:
        sotify = "Yes"
    owners = [str(ids) for ids in config.OWNER_ID]
    owner_id = " ,".join(owners)
    tg_aud = convert_bytes(config.TG_AUDIO_FILESIZE_LIMIT)
    tg_vid = convert_bytes(config.TG_VIDEO_FILESIZE_LIMIT)
    text = f"""🤖 **Bᴏᴛ Iɴғᴏʀᴍᴀꜱɪ:**
**✣ `OWNER_ID`** -≽ **{owner_id}**
**✣ `DURATION_LIMIT`** -≽ **{play_duration} Menit**
**✣ `MUSIC_BOT_NAME`** -≽ **{bot_name}**
**✣ `CLEANMODE_MINS`** -≽ **{cm} Mᴇɴɪᴛ**
**✣ `VIDEO_STREAM_LIMIT`** -≽ **{v_limit} Obrolan**
**✣ `ASSISTANT_LEAVE_TIME`** -≽ **{auto_leave} Detik**
**✣ `AUTO_SUGGESTION_TIME`** -≽ **{auto_sug} Detik**
**✣ `AUTO_SUGGESTION_MODE`** -≽ ** {a_sug}**
**✣ `AUTO_LEAVING_ASSISTANT`** -≽ **{ass}**
**✣ `SONG_DOWNLOAD_DURATION_LIMIT`** -≽ ** {song} Menit**
    """
    await asyncio.sleep(1)
    await mystic.edit_text(text)
