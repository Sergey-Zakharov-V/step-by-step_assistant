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

step_1 = 'Регистрация кабинета на платформе "Royal Family"\nhttps://teletype.in/@royalfamily.club/cknPArFFYTk'

step_2 = "<b>Пополнение личного кабинета Royal Family</b>\n\nhttps://teletype.in/@royalfamily.club/9-I-kDTdU8w"

step_3 = """
<b>Регистрация у брокера</b>

Выберите брокера, которого будете использовать в торговле. Если вы не знаете, обратитесь за помощью к своему куратору, либо в техническую поддержку RF.
"""

step_4 = """
<b>Открытие торгового счета</b>

Выберите брокера для открытия счета и следуйте инструкции.

RoboForex:
https://teletype.in/@royalfamily.club/sozdanie_scheta_robo

Forex4You:
https://teletype.in/@royalfamily.club/RgmjV5MDHBD
"""

step_5 = """
<b>Пополнение торгового счета</b>

Выберите брокера для пополнения счета и следуйте инструкции.

RoboForex: https://teletype.in/@royalfamily.club/popolnenie_robo

Forex4You: https://teletype.in/@royalfamily.club/jxagrJgv0Dc
"""

step_6 = """
<b>Активация и установка робота</b>

Выберите версию робота и следуйте инструкции.

Nova: https://teletype.in/@royalfamily.club/3jcDxKHRHQp

Spider: https://teletype.in/@royalfamily.club/bFNd7tXvN3u
"""

step_7 = """
<b>Важно! На что обращать внимание при роботе с роботом</b>

https://teletype.in/@royalfamily.club/jJbrA8mUqfh
"""

step_8 = """
<b>Вы завершили все шаги необходимые для запуска робота!</b>
Желаем успешного использования и высокой прибыли!

Если вы еще не добавлены в закрытый чат напишите в техническую поддержку для добавления.

Для управления партнерским разделом в боте отправьте сообщение:  /partner
"""
