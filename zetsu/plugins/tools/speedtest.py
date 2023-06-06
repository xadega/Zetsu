import asyncio
import speedtest
from pyrogram import filters
from strings import get_command
from zetsu import app
from zetsu.misc import SUDOERS

# Commands
SPEEDTEST_COMMAND = get_command("SPEEDTEST_COMMAND")


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("**Menjalankan Unduh SpeedTest...**")
        test.download()
        m = m.edit("**Menjalankan Tes Kecepatan Unggah...**")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("**Berbagi Hasil Tes Kecepatan...**")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(filters.command(SPEEDTEST_COMMAND, [".", "(", "-", "!", "/"]) & SUDOERS)
async def speedtest_function(client, message):
    m = await message.reply_text("**Menjalankan Tes Kecepatan...**")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""**📝 Hasil Tes Kecepatan.**
    
<u>**Client:**</u>
**__ISP:__** {result['client']['isp']}
**__Negara:__** {result['client']['country']}
  
<u>**Server:**</u>
**__Nama:__** {result['server']['name']}
**__Negara:__** {result['server']['country']}, {result['server']['cc']}
**__Sponsor:__** {result['server']['sponsor']}
**__Latensi:__** {result['server']['latency']}  
**__Ping:__** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, 
        photo=result["share"], 
        caption=output
    )
    await m.delete()
