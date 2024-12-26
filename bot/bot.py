import redis
import requests
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from constants import (
    API_URL,
    TELEGRAM_TOKEN,
    START_MESSAGE,
    CLEAR_DIALOG_EVENT_NAME,
    USERNAME_KEY,
)

r = redis.Redis(host="redis")
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    greet_kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=CLEAR_DIALOG_EVENT_NAME)],
        ]
    )
    await message.answer(START_MESSAGE, reply_markup=greet_kb)


@dp.message()
async def handle_message(message: Message):
    user_text = message.text
    user_id = message.from_user.id

    if user_text == CLEAR_DIALOG_EVENT_NAME:
        await r.get(USERNAME_KEY.format(user_id=user_id))

    else:
        try:
            response = requests.post(API_URL, json={"prompt": user_text})
            response.raise_for_status()
            generated_text = str(response.json())
            await message.answer(generated_text)
        except requests.exceptions.RequestException as e:
            await message.answer("Произошла ошибка при генерации ответа.")
            print(f"Error in API request: {e}")


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
