# bot/bot.py
import os
import requests
from aiogram import Bot, Dispatcher
from aiogram.types import Message

API_URL = "http://api:5000/generate"  # URL API контейнера

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")  # Токен для бота
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

# Обработчик всех текстовых сообщений
@dp.message()
async def handle_message(message: Message):
    prompt = message.text
    try:
        response = requests.post(API_URL, json={'prompt': prompt})
        response.raise_for_status()  # Проверка на успешность запроса
        generated_text = response.json()
        await message.answer(generated_text)
    except requests.exceptions.RequestException as e:
        await message.answer("Произошла ошибка при генерации ответа.")
        print(f"Error in API request: {e}")

# Основная функция для запуска бота
async def main():
    dp.include_router(dp)  # Регистрация маршрутов
    await bot.delete_webhook(drop_pending_updates=True)  # Очистка старых обновлений
    await dp.start_polling(bot)  # Запуск бота в режиме polling

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
