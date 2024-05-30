from aiogram import types


async def delete_message(message: types.Message):
    try:
        await message.delete()
    except Exception as e:
        pass
