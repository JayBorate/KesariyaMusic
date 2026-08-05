import asyncio

from app.core.assistant import assistant
from app.core.voice import VoiceManager

GROUP_ID = -1001715140111   # Your Telegram group ID


async def main():
    print("Starting Assistant...")
    await assistant.start()

    voice = VoiceManager(assistant)
    await voice.start()

    print("Attempting to play local file...")

    await voice.play_local(
        GROUP_ID,
        "music/test.mp3"
    )

    print("✅ Command sent successfully!")

    input("Press Enter to stop...")

    await assistant.stop()


asyncio.run(main())