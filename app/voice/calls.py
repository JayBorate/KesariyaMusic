from pytgcalls import PyTgCalls
from pytgcalls.types import MediaStream, GroupCallConfig


class VoiceCallManager:
    def __init__(self, assistant):
        self.assistant = assistant
        self.client = PyTgCalls(assistant)

    async def start(self):
        await self.client.start()
        print("🎤 Voice Engine Started")

    async def join_voice_chat(self, chat_id):
        print(f"📞 Ready to join voice chat in {chat_id}")

    async def leave_voice_chat(self, chat_id):
        try:
            await self.client.leave_call(chat_id)
            print("👋 Left voice chat")
        except Exception as e:
            print(f"Leave failed: {e}")

    async def play_local_file(self, chat_id, file_path):
        stream = MediaStream(
            media_path=file_path,
        )

        await self.client.play(
            chat_id=chat_id,
            stream=stream,
            config=GroupCallConfig(
                auto_start=False
            ),
        )

        print(f"🎵 Playing {file_path}")