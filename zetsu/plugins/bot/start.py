import asyncio

from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from youtubesearchpython.__future__ import VideosSearch

import config
from config import BANNED_USERS
from config.config import OWNER_ID
from strings import get_command, get_string
from zetsu import Telegram, YouTube, app
from zetsu.misc import SUDOERS
from zetsu.plugins.play.playlist import del_plist_msg
from zetsu.plugins.sudo.sudoers import sudoers_list
from zetsu.utils.database import (add_served_chat,
                                       add_served_user,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat)
from zetsu.utils.decorators.language import LanguageStart
from zetsu.utils.inline import (help_pannel, private_panel,
                                     start_pannel)

loop = asyncio.get_running_loop()


@app.on_message(
    filters.command(get_command("START_COMMAND"))
    & filters.private
    & ~filters.edited
    & ~BANNED_USERS
)
@LanguageStart
async def start_comm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_pannel(_)
            return await message.reply_text(
                _["help_1"], reply_markup=keyboard
            )
        if name[0:4] == "song":
            return await message.reply_text(_["song_2"])
        if name[0:3] == "sta":
            m = await message.reply_text(
                "🔎 Mᴇɴɢᴀᴍʙɪʟ Iɴғᴏʀᴍᴀꜱɪ"
            )
            stats = await get_userss(message.from_user.id)
            tot = len(stats)
            if not stats:
                await asyncio.sleep(1)
                return await m.edit(_["ustats_1"])

            def get_stats():
                msg = ""
                limit = 0
                results = {}
                for i in stats:
                    top_list = stats[i]["spot"]
                    results[str(i)] = top_list
                    list_arranged = dict(
                        sorted(
                            results.items(),
                            key=lambda item: item[1],
                            reverse=True,
                        )
                    )
                if not results:
                    return m.edit(_["ustats_1"])
                tota = 0
                videoid = None
                for vidid, count in list_arranged.items():
                    tota += count
                    if limit == 10:
                        continue
                    if limit == 0:
                        videoid = vidid
                    limit += 1
                    details = stats.get(vidid)
                    title = (details["title"][:35]).title()
                    if vidid == "telegram":
                        msg += f"💽 [Telegram Files and Audios](https://t.me/telegram) ** played {count} times**\n\n"
                    else:
                        msg += f"💭 [{title}](https://www.youtube.com/watch?v={vidid}) ** played {count} times**\n\n"
                msg = _["ustats_2"].format(tot, tota, limit) + msg
                return videoid, msg

            try:
                videoid, msg = await loop.run_in_executor(
                    None, get_stats
                )
            except Exception as e:
                print(e)
                return
            thumbnail = await YouTube.thumbnail(videoid, True)
            await m.delete()
            await message.reply_photo(photo=thumbnail, caption=msg)
            return
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention} Bᴀʀᴜ Sᴀᴊᴀ Mᴇᴍᴜʟᴀɪ Bᴏᴛ Uɴᴛᴜᴋ Mᴇᴍᴇʀɪᴋꜱᴀ <code>Dᴀғᴛᴀʀ Sᴜᴅᴏ</code>\n\n**🆔 Iᴅ Pᴇɴɢɢᴜɴᴀ -≽ **{sender_id}\n**👤 Nᴀᴍᴀ Pᴇɴɢɢᴜɴᴀ -≽ **{sender_name}",
                )
            return
        if name[0:3] == "lyr":
            query = (str(name)).replace("lyrics_", "", 1)
            lyrical = config.lyrical
            lyrics = lyrical.get(query)
            if lyrics:
                return await Telegram.send_split_text(message, lyrics)
            else:
                return await message.reply_text(
                    "Gagal mendapatkan lirik."
                )
        if name[0:3] == "del":
            await del_plist_msg(client=client, message=message, _=_)
        if name[0:3] == "inf":
            m = await message.reply_text("🔎 Mᴇɴɢᴀᴍʙɪʟ Iɴғᴏ!")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[
                    0
                ]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = f"""
🔎 **Iɴғᴏʀᴍᴀꜱɪ ᴛʀᴇᴋ ᴠɪᴅᴇᴏ**

💭 **Jᴜᴅᴜʟ -≽ ** {title}

⏳ **Dᴜʀᴀꜱɪ -≽ ** {duration}
👀 **Dɪʟɪʜᴀᴛ -≽ ** `{views}`
💬 **Lɪɴᴋ Vɪᴅᴇᴏ -≽ ** [Link]({link})
⏰ **Wᴀᴋᴛᴜ Pᴜʙʟɪꜱʜ -≽ ** {published}
💌 **Nᴀᴍᴀ Cʜᴀɴɴᴇʟ -≽ ** {channel}
💡 **Lɪɴᴋ Cʜᴀɴɴᴇʟ -≽ ** [Visit From Here]({channellink})

🤖 Sᴇᴀʀᴄʜᴇᴅ Pᴏᴡᴇʀᴇᴅ Bʏ {config.MUSIC_BOT_NAME}"""
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="📡 ᴡᴀᴛᴄʜ", url=f"{link}"
                        ),
                        InlineKeyboardButton(
                            text="🗑️ ᴄʟᴏsᴇ", callback_data="close"
                        ),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                parse_mode="markdown",
                reply_markup=key,
            )
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention} Bᴀʀᴜ Sᴀᴊᴀ Mᴇᴍᴜʟᴀɪ Bᴏᴛ Uɴᴛᴜᴋ Mᴇᴍᴇʀɪᴋꜱᴀ <code>Iɴғᴏʀᴍᴀꜱɪ ᴠɪᴅᴇᴏ</code>\n\n**🆔 Iᴅ Pᴇɴɢɢᴜɴᴀ -≽ **{sender_id}\n**👤 Nᴀᴍᴀ Pᴇɴɢɢᴜɴᴀ -≽ **{sender_name}",
                )
    


@app.on_message(filters.command("mstart", [".", "^", "-", "!", "/"])
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@LanguageStart
async def testbot(client, message: Message, _):
    out = start_pannel(_)
    return await message.reply_text(
        _["start_1"].format(
            message.chat.title, config.MUSIC_BOT_NAME
        ),
        reply_markup=InlineKeyboardMarkup(out),
    )


welcome_group = 2

@app.on_message(filters.new_chat_members, group=welcome_group)
async def welcome(client, message: Message):
    chat_id = message.chat.id
    if config.PRIVATE_BOT_MODE == str(True):
        if not await is_served_private_chat(message.chat.id):
            await message.reply_text(
                "**Bot Musik Pribadi**\n\nHanya untuk obrolan resmi dari pemiliknya. Minta pemilik saya untuk mengizinkan obrolan Anda terlebih dahulu."
            )
            return await app.leave_chat(message.chat.id)
    else:
        await add_served_chat(chat_id)
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if member.id == app.id:
                chat_type = message.chat.type
                if chat_type != "supergroup":
                    await message.reply_text(_["start_6"])
                    return await app.leave_chat(message.chat.id)
                if chat_id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_7"].format(
                            f"https://t.me/{app.username}?start=sudolist"
                        )
                    )
                    return await app.leave_chat(chat_id)
                userbot = await get_assistant(message.chat.id)
                out = start_pannel(_)
                await message.reply_text(
                    _["start_3"].format(
                        config.MUSIC_BOT_NAME,
                        userbot.username,
                        userbot.id,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
            if member.id in config.OWNER_ID:
                return await message.reply_text(
                    _["start_4"].format(
                        config.MUSIC_BOT_NAME, member.mention
                    )
                )
            if member.id in SUDOERS:
                return await message.reply_text(
                    _["start_5"].format(
                        config.MUSIC_BOT_NAME, member.mention
                    )
                )
            return
        except:
            return
