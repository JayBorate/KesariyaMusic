import asyncio

from app.core.assistant import assistant
from app.core.voice import VoiceManager


async def main():
    print("Starting Assistant...")
    await assistant.start()

    print("Starting Voice Engine...")
    voice = VoiceManager(assistant)
    await voice.start()

    print("✅ Everything started successfully!")

    await assistant.stop()


asyncio.run(main())