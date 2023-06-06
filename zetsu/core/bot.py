import sys

from pyrogram import Client

import config

from ..logging import LOGGER


class zetsu(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Mulai Bot")
        super().__init__(
            ":memory:",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        try:
            await self.send_message(
                config.LOG_GROUP_ID, "🤖 **Bot Activated**!"
            )
        except:
            LOGGER(__name__).error(
                "Bot gagal mengakses Grup log.  Pastikan Anda telah menambahkan bot Anda ke saluran log Anda dan dipromosikan sebagai admin!!"
            )
            sys.exit()
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != "administrator":
            LOGGER(__name__).error(
                "Silakan promosikan Bot sebagai Admin di Grup Logger!"
            )
            sys.exit()
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        LOGGER(__name__).info(f"Bot Musik Dimulai Sebagai {self.name}")
