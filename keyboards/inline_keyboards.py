from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Да", callback_data="start_yes"),
        InlineKeyboardButton(text="Нет", callback_data="start_no"),
    ]
])

step_1_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад", callback_data="step_1_back"),
        InlineKeyboardButton(text="Продолжить", callback_data="step_1_continue"),
    ]
])

step_2_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад", callback_data="step_2_back"),
        InlineKeyboardButton(text="Продолжить", callback_data="step_2_continue"),
    ]
])

step_3_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад", callback_data="step_3_back"),
        InlineKeyboardButton(text="Продолжить", callback_data="step_3_continue"),
    ]
])

step_4_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад", callback_data="step_4_back"),
        InlineKeyboardButton(text="Продолжить", callback_data="step_4_continue")
    ]
])

step_5_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад", callback_data="step_5_back"),
        InlineKeyboardButton(text="Продолжить", callback_data="step_5_continue"),
    ]
])

step_6_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад", callback_data="step_6_back"),
        InlineKeyboardButton(text="Продолжить", callback_data="step_6_continue"),
    ]
])

step_7_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад", callback_data="step_7_back"),
        InlineKeyboardButton(text="Продолжить", callback_data="step_7_continue"),
    ]
])

step_8_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад", callback_data="step_8_back"),
        InlineKeyboardButton(text="Продолжить", callback_data="step_8_continue"),
    ]
])

step_9_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад", callback_data="step_9_back"),
        InlineKeyboardButton(text="Продолжить", callback_data="step_9_continue"),
    ]
])

step_10_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад", callback_data="step_10_back"),
        InlineKeyboardButton(text="Продолжить", callback_data="step_10_continue"),
    ]
])

important_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад", callback_data="important_back"),
    ]
])
