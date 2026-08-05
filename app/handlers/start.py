from pyrogram import filters


async def start_command(client, message):
    await message.reply_text(
        "🎵 Hello!\n\n"
        "Welcome to Kesariya Music Bot.\n"
        "I'm online and ready to play high-quality music! 🚀"
    )


def register_handlers(app):
    app.add_handler(
        filters.command("start"),
        start_command
    )