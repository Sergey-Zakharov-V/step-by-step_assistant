from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Да", callback_data="start_yes"),
        InlineKeyboardButton(text="Нет", callback_data="start_no"),
    ]
])

step_0_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад", callback_data="step_0_back"),
        InlineKeyboardButton(text="Продолжить", callback_data="step_0_continue"),
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

change_links_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Изменить ссылку на RoyalFamily", callback_data="change_royalfamily"),
    ],
    [
        InlineKeyboardButton(text="Изменить ссылку на RoboForex", callback_data="change_roboforex"),
    ],
    [
        InlineKeyboardButton(text="Изменить ссылку на Forex4You", callback_data="change_forex4you"),
    ],
    [
        InlineKeyboardButton(text="Связаться с техподдержкой", url="https://t.me/RoyalFamily_Support_bot"),
    ]
])

change_link_cancel_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад", callback_data="change_link_cancel"),
    ]
])
