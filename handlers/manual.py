from aiogram import types, F
from aiogram.filters import CommandStart

from data.config import start_message, step_1, step_2, step_3, step_4, step_5, step_6, step_7, step_0
from keyboards.manual_inline_keyboards import start_keyboard, step_1_keyboard, step_2_keyboard, step_3_keyboard, \
    step_4_keyboard, step_5_keyboard, step_6_keyboard, step_7_keyboard, step_0_keyboard, \
    step_3_roboforex_forex4you_keyboard
from main_step_by_step_assistant import dp
from service.users_service import UserService


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


@dp.callback_query(F.data == "step_0_continue")
async def step_1_continue(call: types.CallbackQuery):
    await call.message.delete()

    telegram_id = str(call.message.chat.id)
    user = await UserService.find_one_or_none(**{"telegram_id": telegram_id})
    friend = await UserService.find_one_or_none(**{"telegram_id": user.friend})
    link_royalfamily = friend.link_royalfamily if friend and friend.link_royalfamily else "https://royalfamily.club/login"

    await call.message.answer(
        text=f'Регистрация кабинета на платформе "Royal Family"\nhttps://teletype.in/@royalfamily.club/cknPArFFYTk\n\n{link_royalfamily}',
        reply_markup=step_1_keyboard)


# Step 1
@dp.callback_query(F.data == "step_1_back")
async def step_1_back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=start_message, reply_markup=start_keyboard)


@dp.callback_query(F.data == "step_1_continue")
async def step_1_continue(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=step_2, reply_markup=step_2_keyboard)


# Step 2
@dp.callback_query(F.data == "step_2_back")
async def step_2_back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=step_1, reply_markup=step_1_keyboard)


@dp.callback_query(F.data == "step_2_continue")
async def step_2_continue(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=step_3, reply_markup=step_3_keyboard)


# Step 3
@dp.callback_query(F.data == "step_3_back")
async def step_3_back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=step_2, reply_markup=step_2_keyboard)


@dp.callback_query(F.data == "step_3_roboforex")
async def step_3_back(call: types.CallbackQuery):
    await call.message.delete()

    telegram_id = str(call.message.chat.id)
    user = await UserService.find_one_or_none(**{"telegram_id": telegram_id})
    friend = await UserService.find_one_or_none(**{"telegram_id": user.friend})
    link_roboforex = friend.link_roboforex if friend and friend.link_roboforex else "https://my.roboforex.com/en/login/?a=ooem"

    await call.message.answer(text=f"https://teletype.in/@royalfamily.club/registraciya_robo\n\nRoboForex: {link_roboforex}",
                              reply_markup=step_3_roboforex_forex4you_keyboard)


@dp.callback_query(F.data == "step_3_forex4you")
async def step_3_back(call: types.CallbackQuery):
    await call.message.delete()

    telegram_id = str(call.message.chat.id)
    user = await UserService.find_one_or_none(**{"telegram_id": telegram_id})
    friend = await UserService.find_one_or_none(**{"telegram_id": user.friend})
    link_forex4you = friend.link_forex4you if friend and friend.link_forex4you else "https://forex4you.xyz/?affid=gf60e6x"

    await call.message.answer(text=f"https://teletype.in/@royalfamily.club/oGUU_BSAGMD\n\nForex4You: {link_forex4you}",
                              reply_markup=step_3_roboforex_forex4you_keyboard)


@dp.callback_query(F.data == "step_3_continue")
async def step_3_continue(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=step_4, reply_markup=step_4_keyboard)


# Step 4
@dp.callback_query(F.data == "step_4_back")
async def step_4_back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=step_3, reply_markup=step_3_keyboard)


@dp.callback_query(F.data == "step_4_continue")
async def step_2_continue(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=step_5, reply_markup=step_5_keyboard)


# Step 5
@dp.callback_query(F.data == "step_5_back")
async def step_5_back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=step_4, reply_markup=step_4_keyboard)


@dp.callback_query(F.data == "step_5_continue")
async def step_2_continue(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=step_6, reply_markup=step_6_keyboard)


# Step 6
@dp.callback_query(F.data == "step_6_back")
async def step_5_back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=step_5, reply_markup=step_5_keyboard)


@dp.callback_query(F.data == "step_6_continue")
async def step_2_continue(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=step_7, reply_markup=step_7_keyboard)


# Step 7
@dp.callback_query(F.data == "step_7_back")
async def step_5_back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=step_6, reply_markup=step_6_keyboard)
