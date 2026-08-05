from pyrogram import Client
from dotenv import load_dotenv
import os

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

app = Client(
    "assistant",
    api_id=API_ID,
    api_hash=API_HASH,
)

with app:
    me = app.get_me()
    print("=" * 40)
    print("✅ Assistant session created successfully!")
    print(f"Logged in as: {me.first_name}")
    print(f"User ID: {me.id}")
    print("=" * 40)