from aiogram import types, F
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data.config import start_message, step_2, step_3, step_0
from keyboards.inline_keyboards import start_keyboard, step_1_keyboard, step_2_keyboard, step_0_keyboard
from main_step_by_step_assistant import dp, bot
from service.users_service import UserService


async def get_step_3_keyboard(message: types.Message):
    buttons = [[
        InlineKeyboardButton(text="RoboForex", callback_data="step_3_roboforex_question"),
        InlineKeyboardButton(text="Forex4You", callback_data="step_3_forex4you_question"),
    ]]

    telegram_id = str(message.chat.id)
    user = await UserService.find_one_or_none(**{"telegram_id": telegram_id})
    friend = await UserService.find_one_or_none(**{"telegram_id": user.friend})

    if friend and friend.username:
        buttons.append([
            InlineKeyboardButton(text="Написать куратору", url=f"https://t.me/{friend.username}")
        ])

    buttons.append([
        InlineKeyboardButton(text="Написать в техподдержку", url="https://t.me/RoyalFamily_Support_bot")
    ])

    buttons.append([
        InlineKeyboardButton(text="Назад", callback_data="step_3_back"),
    ])

    return InlineKeyboardMarkup(inline_keyboard=buttons)


# Start
@dp.message(CommandStart())
async def start(message: types.Message):
    await message.delete()

    deep_link = message.text.split(" ")

    username = message.from_user.username
    telegram_id = str(message.chat.id)
    friend = deep_link[1] if len(deep_link) > 1 else None

    user = await UserService.find_one_or_none(**{"telegram_id": telegram_id})
    if user is None:
        await UserService.add(**{"username": username, "telegram_id": telegram_id, "friend": friend})

    if user and friend:
        await UserService.update(object_id=user.id, **{"friend": friend})
    if user and username and not user.username:
        await UserService.update(object_id=user.id, **{"username": username})

    await message.answer(text=start_message, reply_markup=start_keyboard)


@dp.callback_query(F.data == "start_no")
async def start_no(call: types.CallbackQuery):
    await call.message.answer(
        text="Вы можете ознакомится с нашими торговыми системами в этом боте \nhttps://t.me/INFO_RF_bot")


@dp.callback_query(F.data == "start_yes")
async def start_yes(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=step_0, reply_markup=step_0_keyboard)


# Step 0
@dp.callback_query(F.data == "step_0_back")
async def step_0_back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=start_message, reply_markup=start_keyboard)


@dp.callback_query(F.data == "step_2_back")
@dp.callback_query(F.data == "step_0_continue")
async def step_1_continue(call: types.CallbackQuery):
    await call.message.delete()

    telegram_id = str(call.message.chat.id)
    user = await UserService.find_one_or_none(**{"telegram_id": telegram_id})
    friend = await UserService.find_one_or_none(**{"telegram_id": user.friend})
    link_royalfamily = friend.link_royalfamily if friend and friend.link_royalfamily else "https://royalfamily.club/register"

    text = f"""
<b>ШАГ 1/6. Регистрация кабинета RF</b>

В первую очередь надо зарегистрироваться на платформе «Royal Family». Для этого перейдите по ссылке:

{link_royalfamily}

В форме регистрации введите свою электронную почту, никнейм, телеграм и пароль. Примите условия соглашения и нажмите кнопку «Зарегистрироваться»
"""
    try:
        await bot.send_photo(chat_id=call.message.chat.id,
                             caption=text,
                             photo="AgACAgIAAxkBAAICfGZHNfk4758O9rCktzf7l_UTkZ45AAIY3DEbTg85SuUS8KOJNIwAAQEAAwIAA3kAAzUE",
                             reply_markup=step_1_keyboard)
    except TelegramBadRequest:
        await call.message.answer(text=text,
                                  reply_markup=step_1_keyboard)


# Step 1
@dp.callback_query(F.data == "step_1_back")
async def step_1_back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=start_message, reply_markup=start_keyboard)


@dp.callback_query(F.data == "step_3_back")
@dp.callback_query(F.data == "step_1_continue")
async def step_1_continue(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=step_2, reply_markup=step_2_keyboard)


@dp.callback_query(F.data == "step_4_back")
@dp.callback_query(F.data == "step_2_continue")
async def step_2_continue(call: types.CallbackQuery):
    await call.message.delete()
    keyboard = await get_step_3_keyboard(call.message)
    await call.message.answer(text=step_3, reply_markup=keyboard)


@dp.callback_query(F.data == "step_3_roboforex_question")
async def step_3_roboforex_question(call: types.CallbackQuery):
    await call.message.delete()

    text = """
<b>Регистрация у брокера RoboForex</b>

Регистрировались ли Вы ранее на брокере RoboForex?    
"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Да", callback_data="step_3_roboforex_yes"),
            InlineKeyboardButton(text="Нет", callback_data="step_3_roboforex_no")
        ]
    ])
    await call.message.answer(text=text, reply_markup=keyboard)


@dp.callback_query(F.data == "step_3_roboforex_yes")
@dp.callback_query(F.data == "step_3_roboforex_no")
async def step_3_roboforex(call: types.CallbackQuery):
    await call.message.delete()

    question_result = call.data

    telegram_id = str(call.message.chat.id)
    user = await UserService.find_one_or_none(**{"telegram_id": telegram_id})
    friend = await UserService.find_one_or_none(**{"telegram_id": user.friend})
    link_roboforex = friend.link_roboforex if friend and friend.link_roboforex else "https://my.roboforex.com/en/login/?a=ooem"

    text = f"""
    
<b>Регистрация у брокера RoboForex</b>

{"Для регистрации перейдите по этой ссылке:" if question_result == "step_3_roboforex_no" else "Для создания нового аккаунта перейдите по этой ссылке:"}

{link_roboforex}

и выполните все действия в соответствии с инструкцией
{"https://teletype.in/@royalfamily.club/registraciya_robo" if question_result == "step_3_roboforex_no" else "https://teletype.in/@royalfamily.club/registraciya_robo2"}
"""

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад", callback_data="step_4_back"),
            InlineKeyboardButton(text="Продолжить", callback_data=f"step_3_continue_roboforex"),
        ]
    ])

    await call.message.answer(text=text,
                              reply_markup=keyboard)


@dp.callback_query(F.data == "step_3_forex4you_question")
async def step_3_forex4you_question(call: types.CallbackQuery):
    await call.message.delete()

    text = """
<b>Регистрация у брокера Forex4you</b>

Регистрировались ли Вы ранее на брокере Forex4you?   
"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Да", callback_data="step_3_forex4you_yes"),
            InlineKeyboardButton(text="Нет", callback_data="step_3_forex4you_no")
        ]
    ])
    await call.message.answer(text=text, reply_markup=keyboard)


@dp.callback_query(F.data == "step_3_forex4you_yes")
@dp.callback_query(F.data == "step_3_forex4you_no")
async def step_3_forex4you(call: types.CallbackQuery):
    await call.message.delete()

    question_result = call.data

    telegram_id = str(call.message.chat.id)
    user = await UserService.find_one_or_none(**{"telegram_id": telegram_id})
    friend = await UserService.find_one_or_none(**{"telegram_id": user.friend})
    link_forex4you = friend.link_forex4you if friend and friend.link_forex4you else "https://forex4you.xyz/?affid=gf60e6x"

    if question_result == "step_3_forex4you_no":
        text = f"""
<b>Регистрация у брокера Forex4you</b>

Для регистрации перейдите по этой ссылке {link_forex4you}

и выполните все действия в соответствии с инструкцией https://teletype.in/@royalfamily.club/hHnB2OZ-6_E 
"""
    else:
        text = f"""
<b>Перенос аккаунта Forex4you</b>

Для того чтобы работали торговые роботы на брокере Forex4you необходимо перейти в партнерскую сеть Royal Family. 
Для перехода используйте эту ссылку 
{link_forex4you} в соответствии с инструкцией ниже.

Выполните все действия по этой инструкции
https://teletype.in/@royalfamily.club/kkzLUUEiSuC 
"""

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад", callback_data="step_4_back"),
            InlineKeyboardButton(text="Продолжить", callback_data=f"step_3_continue_forex4you"),
        ]
    ])

    await call.message.answer(text=text,
                              reply_markup=keyboard)


@dp.callback_query(F.data == "step_5_back_roboforex")
@dp.callback_query(F.data == "step_3_continue_roboforex")
@dp.callback_query(F.data == "step_5_back_forex4you")
@dp.callback_query(F.data == "step_3_continue_forex4you")
async def step_3_continue(call: types.CallbackQuery):
    await call.message.delete()

    data = call.data.split("_")[3]

    text = f"""
<b>ШАГ 4/6. Открытие личного торгового счета на {"RoboForex" if data == "roboforex" else "Forex4you"}</b>

В этом шаге я помогу вам открыть счет, на котором будет происходить торговля вашим роботом. Хочу напомнить, что доступ к счету, пополнению и снятию средств имеете только вы.

Ниже прикрепляю инструкцию:
{"https://teletype.in/@royalfamily.club/sozdanie_scheta_robo" if data == "roboforex" else "https://teletype.in/@royalfamily.club/RgmjV5MDHBD"}
"""

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад", callback_data="step_4_back"),
            InlineKeyboardButton(text="Продолжить", callback_data=f"step_4_continue_{data}")
        ]
    ])

    await call.message.answer(text=text, reply_markup=keyboard)


@dp.callback_query(F.data == "step_6_back_roboforex")
@dp.callback_query(F.data == "step_4_continue_roboforex")
@dp.callback_query(F.data == "step_6_back_forex4you")
@dp.callback_query(F.data == "step_4_continue_forex4you")
async def step_4_continue(call: types.CallbackQuery):
    await call.message.delete()

    data = call.data.split("_")[3]

    text = f"""
<b>ШАГ 5/6. Пополнение торгового счета {"RoboForex" if data == "roboforex" else "Forex4you"}</b>

Поздравляем! Вы уже открыли счет и стали на шаг ближе к запуску робота. Теперь вам нужно пополнить свой торговый счет на сумму, которая будет удобна для вас.

Обратите внимание, что минимальная сумма для запуска робота в торговлю составляет 100$. Если у вас возникли вопросы или вам нужна помощь, не стесняйтесь обращаться к вашему пригласителю или в нашу техническую поддержку.

Ниже прикрепляю инструкцию:
{"https://teletype.in/@royalfamily.club/popolnenie_robo" if data == "roboforex" else "https://teletype.in/@royalfamily.club/jxagrJgv0Dc"}
"""

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад", callback_data=f"step_5_back_{data}"),
            InlineKeyboardButton(text="Продолжить", callback_data=f"step_5_continue_{data}"),
        ]
    ])

    await call.message.answer(text=text, reply_markup=keyboard)


@dp.callback_query(F.data == "step_7_back_roboforex")
@dp.callback_query(F.data == "step_5_continue_roboforex")
@dp.callback_query(F.data == "step_7_back_forex4you")
@dp.callback_query(F.data == "step_5_continue_forex4you")
async def step_5_continue(call: types.CallbackQuery):
    await call.message.delete()

    data = call.data.split("_")[3]

    text = """
<b>ШАГ 6/6. Запуск робота</b>

Остался последний шаг - запустить робота, чтобы он начал торговать. До первой прибыльной сделки осталось совсем немного.

Инструкцию прикрепляю ниже:
https://teletype.in/@royalfamily.club/3jcDxKHRHQp
"""

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад", callback_data=f"step_6_back_{data}"),
            InlineKeyboardButton(text="ВАЖНО", callback_data=f"step_6_continue_{data}"),
        ]
    ])

    await call.message.answer(text=text, reply_markup=keyboard)


@dp.callback_query(F.data == "step_8_back_roboforex")
@dp.callback_query(F.data == "step_6_continue_roboforex")
@dp.callback_query(F.data == "step_8_back_forex4you")
@dp.callback_query(F.data == "step_6_continue_forex4you")
async def step_6_continue(call: types.CallbackQuery):
    await call.message.delete()

    data = call.data.split("_")[3]

    text = """
<b>Важно! На что обращать внимание при роботе с роботом</b>

https://teletype.in/@royalfamily.club/jJbrA8mUqfh    
"""

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад", callback_data=f"step_7_back_{data}"),
            InlineKeyboardButton(text="Продолжить", callback_data=f"step_7_continue_{data}"),
        ]
    ])

    await call.message.answer(text=text, reply_markup=keyboard)


@dp.callback_query(F.data == "step_7_continue_roboforex")
@dp.callback_query(F.data == "step_7_continue_forex4you")
async def step_7_continue(call: types.CallbackQuery):
    await call.message.delete()

    data = call.data.split("_")[3]

    text = """
<b>Вы завершили все шаги необходимые для запуска робота!</b>
Желаем успешного использования и высокой прибыли!

Если вы еще не добавлены в закрытый чат напишите в техническую поддержку для добавления.

Для управления партнерским разделом в боте отправьте сообщение:  /partner
"""

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Написать в техподдержку", url="https://t.me/RoyalFamily_Support_bot")
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data=f"step_8_back_{data}"),
        ],
    ])

    await call.message.answer(text=text, reply_markup=keyboard)


@dp.message()
async def get_file(message: types.Message):
    if str(message.chat.id) == "1509045389":
        if message.photo:
            print(message.photo)
            await message.answer(f"Photo id: {message.photo[-1].file_id}")
        elif message.video:
            print(message.video)
            await message.answer(f"Video id: {message.video.file_id}")
        elif message.document:
            print(message.document)
            await message.answer(f"Document id: {message.document.file_id}")
