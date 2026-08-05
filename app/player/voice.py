from pyrogram import Client
from pytgcalls import PyTgCalls

class VoiceManager:
    def __init__(self, assistant: Client):
        self.assistant = assistant
        self.call = PyTgCalls(assistant)

    async def start(self):
        await self.call.start()
        print("🎵 Voice engine started successfully!")