from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="Pᴀᴜꜱᴇ Sᴛʀᴇᴀᴍ",
            description=f"Jeda pemutaran saat ini pada obrolan grup.",
            thumb_url="https://telegra.ph/file/c0a1c789def7b93f13745.png",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="Rᴇꜱᴜᴍᴇ Sᴛʀᴇᴀᴍ",
            description=f"Melanjutkan pemutaran saat ini pada obrolan grup.",
            thumb_url="https://telegra.ph/file/02d1b7f967ca11404455a.png",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="Mᴜᴛᴇ Sᴛʀᴇᴀᴍ",
            description=f"Membisukan pemutaran saat ini pada obrolan grup.",
            thumb_url="https://telegra.ph/file/66516f2976cb6d87e20f9.png",
            input_message_content=InputTextMessageContent("/musicmute"),
        ),
        InlineQueryResultArticle(
            title="Uɴᴍᴜᴛᴇ Sᴛʀᴇᴀᴍ",
            description=f"Membunyikan pemutaran saat ini pada obrolan grup.",
            thumb_url="https://telegra.ph/file/3078794f9341ffd582e18.png",
            input_message_content=InputTextMessageContent("/musicunmute"),
        ),
        InlineQueryResultArticle(
            title="Sᴋɪᴘ Sᴛʀᴇᴀᴍ",
            description=f"Lewati ke trek berikutnya. | Untuk nomor trek tertentu: /skip [number] ",
            thumb_url="https://telegra.ph/file/98b88e52bc625903c7a2f.png",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="Sᴛᴏᴘ Sᴛʀᴇᴀᴍ",
            description="Menghentikan pemutaran yang sedang berlangsung pada obrolan grup..",
            thumb_url="https://telegra.ph/file/d2eb03211baaba8838cc4.png",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="Sʜᴜғғʟᴇ Sᴛʀᴇᴀᴍ",
            description="Acak daftar trek yang antri.",
            thumb_url="https://telegra.ph/file/7f6aac5c6e27d41a4a269.png",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="Sᴇᴇᴋ Sᴛʀᴇᴀᴍ",
            description="Cari aliran yang sedang berlangsung dengan durasi tertentu.",
            thumb_url="https://telegra.ph/file/cd25ec6f046aa8003cfee.png",
            input_message_content=InputTextMessageContent("/seek"),
        ),
        InlineQueryResultArticle(
            title="Lᴏᴏᴘ Sᴛʀᴇᴀᴍ",
            description="Putar musik yang sedang diputar. | Usage: /loop [enable|disable]",
            thumb_url="https://telegra.ph/file/081c20ce2074ea3e9b952.png",
            input_message_content=InputTextMessageContent("/loop"),
        ),
    ]
)
