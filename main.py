from pyrogram import Client, filters
from decouple import config
from pyrogram.types import Message
import logging
import ai_api
import os

logging.basicConfig(level=logging.INFO)
spell = Speller(lang='ru')
temp_dir = "temp"
initial_context = (
    "" # сюда вписывать как должна писать нейросеть и информация которую она должна знать
)

if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)

def get_user_history_path(user_id):
    return os.path.join(temp_dir, f"{user_id}.txt")

def load_user_history(user_id):
    history_path = get_user_history_path(user_id)
    if os.path.exists(history_path):
        with open(history_path, "r", encoding="utf-8") as file:
            return file.read()
    return initial_context

def save_user_history(user_id, history):
    history_path = get_user_history_path(user_id)
    with open(history_path, "w", encoding="utf-8") as file:
        file.write(history)

bot = Client(name=config('LOGIN'),
             api_id=config('API_ID'),
             api_hash=config('API_HASH'),
             phone_number=config('PHONE'))

@bot.on_message(filters.text)
async def ai_sender(client: Client, message: Message):
    user_id = message.from_user.id
    history = load_user_history(user_id)
    full_prompt = f"{history}\nUser: {message.text}\nAssistant:"
    ai_answer = ai_api.AI_ollama_api_send(config('URL_OLLAMA'), full_prompt)
    updated_history = f"{full_prompt}\n{ai_answer}"
    save_user_history(user_id, updated_history)
    await client.read_chat_history(chat_id=message.chat.id)
    await client.send_message(chat_id=message.chat.id, text=ai_answer)
    
bot.run()
