from pytgcalls import PyTgCalls


class VoiceManager:
    def __init__(self, assistant):
        self.assistant = assistant
        self.app = PyTgCalls(assistant)

    async def start(self):
        await self.app.start()
        print("🎤 Voice Engine Started")