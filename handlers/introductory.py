from aiogram import F, types
from aiogram.types import CallbackQuery

from data.config import about_the_club_text, for_whom_text, robots_text, profit_text, description_conservative, \
    description_medium, description_spider, profitability_text, reliability_text, how_to_get_started_text
from keyboards.introductory_inline_keyboards import start_keyboard, start_back_keyboard, back_to_start_keyboard, \
    robots_keyboard, profit_keyboard, trading_algorithm_keyboard, back_to_algorithm_keyboard, profitability_keyboard, \
    back_to_profitability_keyboard, reliability_keyboard, back_to_reliability_keyboard, how_to_get_started_keyboard
from main_step_by_step_assistant import dp
from utils.message_delete import delete_message


@dp.callback_query(F.data == "back_to_start")
@dp.callback_query(F.data == "start_no")
async def start_no(call: types.CallbackQuery):
    await delete_message(message=call.message)

    text = "Выберите раздел для ознакомления:"

    await call.message.answer(text=text, reply_markup=start_keyboard)


@dp.callback_query(F.data == "about_the_club")
async def about_the_club(call: CallbackQuery):
    await delete_message(message=call.message)

    await call.message.answer_video(caption=about_the_club_text,
                                    video="BAACAgIAAxkBAAIF8WZUVbq8iUTmZeICGbm7fWR7nWMYAAKtRgAC7SGhSoj8K2bflIsiNQQ",
                                    reply_markup=start_back_keyboard)


@dp.callback_query(F.data == "for_whom")
async def for_whom(call: CallbackQuery):
    await delete_message(message=call.message)

    await call.message.answer_photo(caption=for_whom_text,
                                    photo="AgACAgIAAxkBAAIF82ZUVdUTMwKzSlrfsnQacIO1l6GEAAJS1jEb7SGhSq8EgfCDcj1ZAQADAgADeQADNQQ",
                                    reply_markup=back_to_start_keyboard)


@dp.callback_query(F.data == "robots")
async def robots(call: CallbackQuery):
    await delete_message(message=call.message)

    await call.message.answer_photo(caption=robots_text,
                                    photo="AgACAgIAAxkBAAIF9WZUVexnJ0SygUv0JqCTEOxixtZ-AAJT1jEb7SGhSsZCuy1-Z31vAQADAgADeQADNQQ",
                                    reply_markup=robots_keyboard)


@dp.callback_query(F.data == "profit")
async def profit(call: CallbackQuery):
    await delete_message(message=call.message)

    await call.message.answer(text=profit_text, reply_markup=profit_keyboard)


@dp.callback_query(F.data == "trading_algorithm")
async def trading_algorithm(call: CallbackQuery):
    await delete_message(message=call.message)

    await call.message.answer(text="Выберете торговую систему с которой хотите ознакомиться детальнее.",
                              reply_markup=trading_algorithm_keyboard)


@dp.callback_query(F.data.startswith("algorithm"))
async def algorithm(call: CallbackQuery):
    await delete_message(message=call.message)

    data = call.data.split("_")
    if data[1] == "conservative":
        await call.message.answer(text=description_conservative, reply_markup=back_to_algorithm_keyboard)
    elif data[1] == "medium":
        await call.message.answer(text=description_medium, reply_markup=back_to_algorithm_keyboard)
    elif data[1] == "spider":
        await call.message.answer(text=description_spider, reply_markup=back_to_algorithm_keyboard)


@dp.callback_query(F.data == "profitability")
async def profitability(call: CallbackQuery):
    await delete_message(message=call.message)

    await call.message.answer_photo(caption=profitability_text,
                                    photo="AgACAgIAAxkBAAIHZWZbXrxQ4NN1PQZyXeG9nL2QgUYjAAKS3jEb_KzZSrUtk9QI-5fuAQADAgADeQADNQQ",
                                    reply_markup=profitability_keyboard)


@dp.callback_query(F.data.startswith("robot_profitability"))
async def robot_profitability(call: CallbackQuery):
    await delete_message(message=call.message)

    data = call.data.split("_")

    photo = None
    if data[2] == "conservative":
        photo = "AgACAgIAAxkBAAINUWaCu5QS58S9tFXA1sBYmZTyToHmAALs3jEbqSsQSBYGjqLgP022AQADAgADeQADNQQ"
    elif data[2] == "conservative+":
        photo = "AgACAgIAAxkBAAINTGaCu5Oucl8_0AwHRE0930PsqaD-AALq3jEbqSsQSIm-jD6nj-9rAQADAgADeQADNQQ"
    elif data[2] == "medium":
        photo = "AgACAgIAAxkBAAINTmaCu5M3NrMlSibCFSb7rIpoBJCNAALr3jEbqSsQSFTAhxWGaE62AQADAgADeQADNQQ"
    elif data[2] == "medium+":
        photo = "AgACAgIAAxkBAAINSWaCu5I0zPj8oGWTilwRQZNXfD_wAALp3jEbqSsQSIvK9plFn3RPAQADAgADeQADNQQ"
    elif data[2] == "spider":
        photo = "AgACAgIAAxkBAAINR2aCu5LlZyqpSCFQrvEdf-Jsu-YLAALn3jEbqSsQSJost8cEpZo7AQADAgADeQADNQQ"
    elif data[2] == "spider+":
        photo = "AgACAgIAAxkBAAINSGaCu5IompuRaQjAeNkSrLwTGBjuAALo3jEbqSsQSBmNVze6odb1AQADAgADeQADNQQ"
    if photo:
        await call.message.answer_photo(photo=photo,
                                        reply_markup=back_to_profitability_keyboard)


@dp.callback_query(F.data == "reliability")
async def reliability(call: CallbackQuery):
    await delete_message(message=call.message)

    await call.message.answer_photo(caption=reliability_text,
                                    photo="AgACAgIAAxkBAAIGBWZUVoN0u6LNfV_AHPCi_O5WiE0fAAJf1jEb7SGhSlNVpjHS4xXHAQADAgADeQADNQQ",
                                    reply_markup=reliability_keyboard)


@dp.callback_query(F.data == "how_the_robot_trades")
async def how_the_robot_trades(call: CallbackQuery):
    await delete_message(message=call.message)

    await call.message.answer(text="https://youtu.be/3sGKzrv_UoY",
                              reply_markup=back_to_reliability_keyboard)


@dp.callback_query(F.data == "how_to_get_started")
async def how_to_get_started(call: CallbackQuery):
    await delete_message(message=call.message)

    await call.message.answer_photo(caption=how_to_get_started_text,
                                    photo="AgACAgIAAxkBAAIGB2ZUVqXJRT7aN49wTVCDoBptTO1RAAJg1jEb7SGhSszfthPghbIUAQADAgADeQADNQQ",
                                    reply_markup=how_to_get_started_keyboard)


@dp.callback_query(F.data == "start")
async def start_cb(call: CallbackQuery):
    await delete_message(message=call.message)

    await call.message.answer(
        text="Если вы узнали о наших торговых системах от кого-то, то вам следует попросить индивидуальную ссылку на регистрацию у этого человека.\nЕсли же вы сами нашли информацию о нас, то просто продолжайте регистрацию в этом боте https://t.me/RFregbot \nЖелаем удачи!")
