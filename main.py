from app.core.bot import bot

from app.commands.start import register as register_start
from app.commands.admin import register as register_admin

register_start(bot)
register_admin(bot)

print("🚀 Starting Kesariya Music Bot...")

bot.run()