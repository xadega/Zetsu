import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from zetsu import LOGGER, app, userbot
from zetsu.core.call import zetsu
from zetsu.plugins import ALL_MODULES
from zetsu.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("Zetsu").error(
            "Tidak Ada Asisten Klien yang Ditentukan Vars!.. Proses Keluar."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("Zetsu").warning(
            "Tidak ada Spotify Vars yang ditentukan.  Bot Anda tidak akan dapat memainkan kueri spotify."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("zetsu.plugins" + all_module)
    LOGGER("zetsu.plugins").info(
        "Modul Berhasil Diimpor"
    )
    await userbot.start()
    await zetsu.start()
    try:
        await zetsu.stream_call(
            "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("Zetsu").error(
            "[ERROR] - \n\nHarap aktifkan Obrolan Suara Grup Logger Anda.  Pastikan Anda tidak pernah menutup/mengakhiri obrolan suara di grup log Anda"
        )
        sys.exit()
    except:
        pass
    await zetsu.decorators()
    LOGGER("Zetsu").info("Zetsu Musik Berhasil Dimulai!")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("Zetsu").info("Menghentikan Zetsu Music! Selamat tinggal!")
