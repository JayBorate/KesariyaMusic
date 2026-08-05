from pyrogram import filters
from config import OWNER_ID

def register(bot):

    @bot.on_message(filters.command("join") & filters.user(OWNER_ID))
    async def join_command(client, message):
        await message.reply_text(
            "✅ Join command received.\n\n"
            "Voice engine will be connected next."
        )

    @bot.on_message(filters.command("leave") & filters.user(OWNER_ID))
    async def leave_command(client, message):
        await message.reply_text(
            "👋 Leave command received."
        )