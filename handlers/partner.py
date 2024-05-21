from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from keyboards.inline_keyboards import change_links_keyboard, change_link_cancel_keyboard
from main_step_by_step_assistant import dp
from service.users_service import UserService


class LinkState(StatesGroup):
    set_link_royalfamily = State()
    set_link_roboforex = State()
    set_link_forex4you = State()


@dp.message(Command("partner"))
async def partner(message: Message):
    if not message.chat.username:
        text = """
Для доступа к партнерской системе необходимо иметь имя пользователя(username) в Telegram

Настроить его можно в настройках

После добавления username отправьте мне команду /start
"""
        await message.answer(text=text)
        return None

    telegram_id = str(message.chat.id)
    user = await UserService.find_one_or_none(**{"telegram_id": telegram_id})

    if not user:
        await message.answer(text="Вам необходимо написать мне /start для продолжения")
        return None

    text = f"""
Ваша партнерская ссылка бота: https://t.me/RFregbot?start={telegram_id}\n

Ваши регистрационные ссылки:
RoyalFamily: {user.link_royalfamily if user.link_royalfamily else 'ссылка не установлена'}
RoboForex: {user.link_roboforex if user and user.link_roboforex else 'ссылка не установлена'}
Forex4You: {user.link_forex4you if user and user.link_forex4you else 'ссылка не установлена'}
"""

    await message.answer(text=text, reply_markup=change_links_keyboard)


@dp.callback_query(F.data == "change_royalfamily")
async def change_royalfamily(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.set_state(LinkState.set_link_royalfamily)
    await call.message.answer("Пришлите мне вашу партнерскую ссылку",
                              reply_markup=change_link_cancel_keyboard)


@dp.message(LinkState.set_link_royalfamily)
async def set_link_royalfamily(message: Message, state: FSMContext):
    await message.delete()
    link = message.text
    telegram_id = str(message.chat.id)
    user = await UserService.find_one_or_none(**{"telegram_id": telegram_id})
    if user:
        if link.startswith("https://"):
            await UserService.update(object_id=user.id, **{"link_royalfamily": link})
            await partner(message)
            await state.clear()
        else:
            await message.answer(text="Необходимо указать корректную ссылку",
                                 reply_markup=change_link_cancel_keyboard)


@dp.callback_query(F.data == "change_roboforex")
async def change_royalfamily(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.set_state(LinkState.set_link_roboforex)
    await call.message.answer("Пришлите мне вашу партнерскую ссылку",
                              reply_markup=change_link_cancel_keyboard)


@dp.message(LinkState.set_link_roboforex)
async def set_link_roboforex(message: Message, state: FSMContext):
    await message.delete()
    link = message.text
    telegram_id = str(message.chat.id)
    user = await UserService.find_one_or_none(**{"telegram_id": telegram_id})
    if user:
        if link.startswith("https://"):
            await UserService.update(object_id=user.id, **{"link_roboforex": link})
            await partner(message)
            await state.clear()
        else:
            await message.answer(text="Необходимо указать корректную ссылку",
                                 reply_markup=change_link_cancel_keyboard)


@dp.callback_query(F.data == "change_forex4you")
async def change_link_forex4you(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.set_state(LinkState.set_link_forex4you)
    await call.message.answer(text="Пришлите мне вашу партнерскую ссылку",
                              reply_markup=change_link_cancel_keyboard)


@dp.message(LinkState.set_link_forex4you)
async def set_link_forex4you(message: Message, state: FSMContext):
    await message.delete()
    link = message.text
    telegram_id = str(message.chat.id)
    user = await UserService.find_one_or_none(**{"telegram_id": telegram_id})
    if user:
        if link.startswith("https://"):
            await UserService.update(object_id=user.id, **{"link_forex4you": link})
            await partner(message)
            await state.clear()
        else:
            await message.answer(text="Необходимо указать корректную ссылку",
                                 reply_markup=change_link_cancel_keyboard)


@dp.callback_query(F.data == "change_link_cancel")
async def change_link_cancel(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.clear()
    await partner(call.message)
