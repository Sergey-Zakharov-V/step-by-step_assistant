from aiogram import types, F
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data.config import start_message, step_1, step_2, step_3, step_4, step_5, step_6, step_7, step_0, step_8
from keyboards.inline_keyboards import start_keyboard, step_1_keyboard, step_2_keyboard, \
    step_4_keyboard, step_5_keyboard, step_6_keyboard, step_7_keyboard, step_0_keyboard, \
    step_3_roboforex_forex4you_keyboard, step_8_keyboard
from main_step_by_step_assistant import dp, bot
from service.users_service import UserService


async def get_step_3_keyboard(message: types.Message):
    buttons = [[
        InlineKeyboardButton(text="RoboForex", callback_data="step_3_roboforex"),
        InlineKeyboardButton(text="Forex4You", callback_data="step_3_forex4you"),
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
        InlineKeyboardButton(text="Продолжить", callback_data="step_3_continue"),
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
        text="Вы можете ознакомится с нашими торговыми системами в этом боте \nhttps://t.me/RFclubbot")


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
    link_royalfamily = friend.link_royalfamily if friend and friend.link_royalfamily else "https://royalfamily.club/login"

    text = f"""
<b>Регистрация кабинета RF</b>

Для регистрации на платформе "Royal Family" перейдите по этой ссылке

{link_royalfamily}

В форме регистрации введите свою электронную почту, никнейм, телеграм и пароль. Примите условия соглашения и нажмите кнопку "Зарегистрироваться"
"""
    await bot.send_photo(chat_id=call.message.chat.id,
                         caption=text,
                         photo="AgACAgIAAxkBAAICfGZHNfk4758O9rCktzf7l_UTkZ45AAIY3DEbTg85SuUS8KOJNIwAAQEAAwIAA3kAAzUE",
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


@dp.callback_query(F.data == "step_3_roboforex")
async def step_3_roboforex(call: types.CallbackQuery):
    await call.message.delete()

    telegram_id = str(call.message.chat.id)
    user = await UserService.find_one_or_none(**{"telegram_id": telegram_id})
    friend = await UserService.find_one_or_none(**{"telegram_id": user.friend})
    link_roboforex = friend.link_roboforex if friend and friend.link_roboforex else "https://my.roboforex.com/en/login/?a=ooem"

    text = f"""
<b>Регистрация у брокера RoboForex</b>

Для регистрации перейдите по этой ссылке {link_roboforex}

и выполните все действия в соответствии с инструкцией https://teletype.in/@royalfamily.club/registraciya_robo
"""

    await call.message.answer(text=text,
                              reply_markup=step_3_roboforex_forex4you_keyboard)


@dp.callback_query(F.data == "step_3_forex4you")
async def step_3_forex4you(call: types.CallbackQuery):
    await call.message.delete()

    telegram_id = str(call.message.chat.id)
    user = await UserService.find_one_or_none(**{"telegram_id": telegram_id})
    friend = await UserService.find_one_or_none(**{"telegram_id": user.friend})
    link_forex4you = friend.link_forex4you if friend and friend.link_forex4you else "https://forex4you.xyz/?affid=gf60e6x"

    text = f"""
<b>Регистрация у брокера Forex4you</b>

Для регистрации перейдите по этой ссылке {link_forex4you}

и выполните все действия в соответствии с инструкцией https://teletype.in/@royalfamily.club/oGUU_BSAGMD    
"""

    await call.message.answer(text=text,
                              reply_markup=step_3_roboforex_forex4you_keyboard)


@dp.callback_query(F.data == "step_5_back")
@dp.callback_query(F.data == "step_3_continue")
async def step_3_continue(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=step_4, reply_markup=step_4_keyboard)


@dp.callback_query(F.data == "step_6_back")
@dp.callback_query(F.data == "step_4_continue")
async def step_4_continue(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=step_5, reply_markup=step_5_keyboard)


@dp.callback_query(F.data == "step_7_back")
@dp.callback_query(F.data == "step_5_continue")
async def step_5_continue(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=step_6, reply_markup=step_6_keyboard)


@dp.callback_query(F.data == "step_8_back")
@dp.callback_query(F.data == "step_6_continue")
async def step_6_continue(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=step_7, reply_markup=step_7_keyboard)


@dp.callback_query(F.data == "step_7_continue")
async def step_7_continue(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=step_8, reply_markup=step_8_keyboard)


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