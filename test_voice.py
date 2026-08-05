import asyncio

from app.core.assistant import assistant
from app.voice.calls import VoiceCallManager


async def main():
    print("🚀 Starting Assistant...")

    await assistant.start()

    me = await assistant.get_me()
    print(f"✅ Logged in as: {me.first_name}")

    print("🎤 Creating Voice Manager...")
    voice = VoiceCallManager(assistant)

    print("▶ Starting Voice Engine...")
    await voice.start()

    print("✅ Voice Engine started successfully!")

    await assistant.stop()


if __name__ == "__main__":
    asyncio.run(main())