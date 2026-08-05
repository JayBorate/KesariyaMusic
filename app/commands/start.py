from pyrogram import filters

def register(bot):
    @bot.on_message(filters.command("start"))
    async def start_command(client, message):
        await message.reply_text(
            "🎵 Hello!\n\n"
            "Welcome to Kesariya Music Bot.\n"
            "I'm online and getting smarter every day! 🚀"
        )

    @bot.on_message(filters.command("id"))
    async def id_command(client, message):
        await message.reply_text(
            f"🆔 Chat ID:\n`{message.chat.id}`"
        )