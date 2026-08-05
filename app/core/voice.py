from pytgcalls import PyTgCalls

class VoiceManager:
    def __init__(self, assistant):
        self.assistant = assistant
        self.app = PyTgCalls(assistant)