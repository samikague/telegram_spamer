from telethon import TelegramClient
from config import load_env

api_id, api_hash = load_env()
client = TelegramClient("foo", api_id, api_hash)

async def get_client_info():
    info = await client.get_me()
    return {
        "id": info.id,
        "first_name": info.first_name,
        "last_name": info.last_name,
        "phone": info.phone,
        "username": info.username,
        "spam": info.restricted
    }