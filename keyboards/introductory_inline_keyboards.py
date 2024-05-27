from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="О клубе", callback_data="about_the_club"),
        ],
        [
            InlineKeyboardButton(text="Для кого", callback_data="for_whom"),
        ],
        [
            InlineKeyboardButton(text="Роботы", callback_data="robots"),
        ],
        [
            InlineKeyboardButton(text="Статистика", callback_data="profitability"),
        ],
        [
            InlineKeyboardButton(text="Надёжность", callback_data="reliability"),
        ],
        [
            InlineKeyboardButton(text="Как начать", callback_data="how_to_get_started"),
        ],
    ]
)

start_back_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Далее", callback_data="for_whom"),
            InlineKeyboardButton(text="Назад", callback_data="back_to_start"),
        ]
    ]
)

back_to_start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Роботы", callback_data="robots"),
            InlineKeyboardButton(text="Назад", callback_data="back_to_start"),
        ]
    ]
)

robots_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Доходность", callback_data="profit"),
            InlineKeyboardButton(text="Назад", callback_data="back_to_start"),
        ]
    ]
)

profit_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Алгоритм торговли", callback_data="trading_algorithm"),
            InlineKeyboardButton(text="Назад", callback_data="back_to_start"),
        ]
    ]
)

trading_algorithm_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Nova Conservative", callback_data="algorithm_conservative"),
        ],
        [
            InlineKeyboardButton(text="Nova Medium", callback_data="algorithm_medium"),
        ],
        [
            InlineKeyboardButton(text="Spider", callback_data="algorithm_spider"),
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="back_to_start"),
        ]
    ]
)

back_to_algorithm_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад", callback_data="trading_algorithm"),
        ]
    ]
)

profitability_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Nova Conservative", callback_data="robot_profitability_conservative"),
        ],
        [
            InlineKeyboardButton(text="Nova Conservative+", callback_data="robot_profitability_conservative+"),
        ],
        [
            InlineKeyboardButton(text="Nova Medium", callback_data="robot_profitability_medium"),
        ],
        [
            InlineKeyboardButton(text="Nova Medium+", callback_data="robot_profitability_medium+"),
        ],
        [
            InlineKeyboardButton(text="Spider Lite", callback_data="robot_profitability_spider"),
        ],
        [
            InlineKeyboardButton(text="Spider Pro", callback_data="robot_profitability_spider+"),
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="back_to_start"),
        ],
    ]
)

back_to_profitability_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад", callback_data="profitability"),
        ]
    ]
)

reliability_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Посмотреть", callback_data="how_the_robot_trades"),
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="back_to_start"),
        ],
    ]
)

back_to_reliability_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад", callback_data="reliability"),
        ]
    ]
)

how_to_get_started_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="У меня вопрос", url="https://t.me/RoyalFamily_Support_bot"),
            InlineKeyboardButton(text="Начать", callback_data="start_yes"),
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="back_to_start"),
        ]
    ]
)
