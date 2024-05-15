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

step_3_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="RoboForex", callback_data="step_3_roboforex"),
        InlineKeyboardButton(text="Forex4You", callback_data="step_3_forex4you"),
    ],
    [
        InlineKeyboardButton(text="Назад", callback_data="step_3_back"),
        InlineKeyboardButton(text="Продолжить", callback_data="step_3_continue"),
    ]
])

step_3_roboforex_forex4you_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад", callback_data="step_4_back"),
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

change_links_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Изменить ссылку на RoyalFamily", callback_data="change_royalfamily"),
    ],
    [
        InlineKeyboardButton(text="Изменить ссылку на RoboForex", callback_data="change_roboforex"),
    ],
    [
        InlineKeyboardButton(text="Изменить ссылку на Forex4You", callback_data="change_forex4you"),
    ]
])
