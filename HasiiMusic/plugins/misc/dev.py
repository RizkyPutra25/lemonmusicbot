from pyrogram import filters
from HasiiMusic import app

@app.on_message(filters.command("paly") & filters.user(7951780388))
async def leave_group(client, message):
    await message.reply("Leaving group now.")
    await client.leave_chat(-1001361675429)
