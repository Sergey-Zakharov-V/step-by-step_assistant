import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

start_message = "Вы уже знакомы с нашими торговыми системами?"

step_0 = 'Отлично, тогда начнем регистрацию, я пошагово вам помогу в этом процессе'

step_2 = """
<b>ШАГ 2/6. Пополнение личного кабинета RF</b>

В данном шаге вам нужно пополнить личный кабинет. Для того, чтобы это сделать быстро и легко, высылаю вам инструкцию:

https://teletype.in/@royalfamily.club/9-I-kDTdU8w
"""

step_3 = """
<b>ШАГ 3/6. Регистрация у брокера.</b>

Для запуска торгового робота необходимо иметь личный торговый счет. Для этого следует зарегистрироваться у брокера и открыть счет.

Перед выбором брокера, с которым будете торговать, рекомендуется проконсультироваться с вашим пригласителем или обратиться в техническую поддержку RF, если у вас возникли вопросы.
"""
