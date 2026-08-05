import asyncio

from app.assistant import assistant
from app.player.voice import VoiceManager


async def main():
    print("🚀 Starting assistant...")

    await assistant.start()

    me = await assistant.get_me()

    print(f"✅ Logged in as: {me.first_name}")

    voice = VoiceManager(assistant)

    await voice.start()

    print("✅ Voice manager is ready.")

    await assistant.stop()


if __name__ == "__main__":
    asyncio.run(main())