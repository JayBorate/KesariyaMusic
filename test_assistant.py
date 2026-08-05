from app.assistant import assistant

print("🚀 Starting Assistant...")

assistant.start()

me = assistant.get_me()

print("=" * 40)
print("✅ Assistant connected!")
print(f"Name : {me.first_name}")
print(f"ID   : {me.id}")
print("=" * 40)

assistant.stop()