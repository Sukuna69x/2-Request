from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest
from bot import Bot
from config import CHANNEL_ONE, CHANNEL_TWO, CHANNEL_THREE
from database.database import add_req_one, add_req_two, add_req_three

@Bot.on_chat_join_request(
    filters.chat(CHANNEL_ONE) | filters.chat(CHANNEL_TWO) | filters.chat(CHANNEL_THREE)
)
async def join_reqs(client, join_req: ChatJoinRequest):
    user_id = join_req.from_user.id
    if join_req.chat.id == CHANNEL_ONE:
        try:
            await add_req_one(user_id)
        except Exception as e:
            print(f"Error adding join request to req_one: {e}")
    elif join_req.chat.id == CHANNEL_TWO:
        try:
            await add_req_two(user_id)
        except Exception as e:
            print(f"Error adding join request to req_two: {e}")

    elif join_req.chat.id == CHANNEL_THREE:
        try:
            await add_req_three(user_id)
        except Exception as e:
            print(f"Error adding join request to req_three: {e}")
            
