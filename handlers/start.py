from aiogram import types, F

from data.config import start_message, step_1, step_2, step_3, step_4, step_5, step_6, step_7, step_8, step_9, step_10
from keyboards.inline_keyboards import start_keyboard, step_1_keyboard, step_2_keyboard, step_3_keyboard, \
    step_4_keyboard, step_5_keyboard, step_6_keyboard, step_7_keyboard, step_8_keyboard, step_9_keyboard, \
    step_10_keyboard, important_keyboard
from main_step_by_step_assistant import dp


# Start
@dp.message()
async def start(message: types.Message):
    await message.delete()
    await message.answer(text=start_message, reply_markup=start_keyboard)


@dp.callback_query(F.data == "start_no")
async def start_no(call: types.CallbackQuery):
    await call.message.answer(text="Ознакомительный бот: https://t.me/RFclubbot")


@dp.callback_query(F.data == "start_yes")
async def start_yes(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=step_1, reply_markup=step_1_keyboard)


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


@dp.callback_query(F.data == "step_7_continue")
async def step_2_continue(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=step_8, reply_markup=step_8_keyboard)


# Step 8
@dp.callback_query(F.data == "step_8_back")
async def step_5_back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=step_7, reply_markup=step_7_keyboard)


@dp.callback_query(F.data == "step_8_continue")
async def step_2_continue(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=step_9, reply_markup=step_9_keyboard)


# Step 9
@dp.callback_query(F.data == "step_9_back")
async def step_5_back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=step_8, reply_markup=step_8_keyboard)


@dp.callback_query(F.data == "step_9_continue")
async def step_2_continue(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=step_10, reply_markup=step_10_keyboard)


# Step 10
@dp.callback_query(F.data == "step_10_back")
async def step_5_back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=step_9, reply_markup=step_9_keyboard)


@dp.callback_query(F.data == "step_10_continue")
async def step_2_continue(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="Важно!", reply_markup=important_keyboard)


@dp.callback_query(F.data == "important_back")
async def step_5_back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=step_10, reply_markup=step_10_keyboard)
