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

step_2 = "Пополнение личного кабинета Royal Family\nhttps://teletype.in/@royalfamily.club/9-I-kDTdU8w"

step_3 = "Регистрация у брокера.\n\nВыберите брокера\n\nЕсли вы не знаете, обратитесь к вашему куратору либо в техническую поддержку."

step_4 = "Открытие торгового счета\nRoboForex: https://teletype.in/@royalfamily.club/sozdanie_scheta_robo\nForex4You: https://teletype.in/@royalfamily.club/RgmjV5MDHBD"

step_5 = "Пополнение торгового счета\nRoboForex: https://teletype.in/@royalfamily.club/popolnenie_robo\nForex4You: https://teletype.in/@royalfamily.club/jxagrJgv0Dc"

step_6 = "Активация и установка робота\nNova: https://teletype.in/@royalfamily.club/3jcDxKHRHQp\nSpider: https://teletype.in/@royalfamily.club/bFNd7tXvN3u"

step_7 = "Важно!\nhttps://teletype.in/@royalfamily.club/jJbrA8mUqfh"
