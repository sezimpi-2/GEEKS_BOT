import asyncio
import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
import random

load_dotenv()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}!")

@dp.message_handler(commands=["photo"])
async def send_random_photo(message: types.Message):

    img_files = os.listdir('images')
    random_photo = random.choice(img_files)
    photo_path = os.path.join('images', random_photo)

    with open(photo_path, 'rb') as photo:
        await message.reply_photo(photo)

async def main():
    await dp.start_polling()
if __name__ == '__main__':

    asyncio.run(main())
