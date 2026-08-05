from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "KesariyaMusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


@app.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text(
        "🎵 Hello!\n\n"
        "Welcome to Kesariya Music Bot.\n"
        "I'm online and ready to play music soon! 🚀"
    )


@app.on_message(filters.command("id"))
async def id_command(client, message):
    await message.reply_text(
        f"🆔 Chat ID:\n`{message.chat.id}`"
    )


print("🚀 Starting Kesariya Music Bot...")

app.run()