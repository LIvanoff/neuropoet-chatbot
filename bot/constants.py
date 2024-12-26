import os

API_URL: str = "http://api:8000/generate"

TELEGRAM_TOKEN: str = os.getenv("TELEGRAM_TOKEN")

START_MESSAGE: str = """
Привет! 
Меня зовут НейроВитя. Если вдруг кожаный оказался занят и не отвечает тебе, то ты всегда можешь написать мне. Мы можем поговорить о высокодуховных материях сего мира либо я могу написать тебе стихотворение.
А если ты хочешь больше знать об Викторе Логинове, то подписывайся на мои соц. сети:
📚 Стихи.ру - https://stihi.ru/avtor/667835
🖥 Группа в ВК - https://vk.com/pc21t
"""

CLEAR_DIALOG_EVENT_NAME: str = "Очистить диалог 🧹"

USERNAME_KEY: str = "username_{user_id}"
