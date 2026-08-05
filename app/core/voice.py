from pytgcalls import PyTgCalls


class VoiceManager:
    def __init__(self, assistant):
        self.assistant = assistant
        self.app = PyTgCalls(assistant)

    async def start(self):
        await self.app.start()
        print("🎤 Voice Engine Started")

    async def play_local(self, chat_id, file_path):
        await self.app.play(chat_id, file_path)
        print(f"🎵 Playing: {file_path}")