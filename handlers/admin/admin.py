from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from data.config import ADMIN_PASSWORD
from loader import dp
from filters import IsPrivate
from states.admin import Admin
from utils.db_api import register_commands as commands


@dp.message_handler(IsPrivate(), Command('admin'))
async def admin_command(message: types.Message):
    text = f'Admin parol:'
    await message.answer(text)
    await Admin.password.set()


@dp.message_handler(IsPrivate(), state=Admin.password)
async def check_admin_command(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(password=answer)
    if answer == ADMIN_PASSWORD:
        user = await commands.select_user_by_id(user_id=message.from_user.id)
        if user:
            await commands.update_is_admin(message.from_user.id)
            await message.answer(f"Hush kelibsiz, admin \n"
                                 f"Yangi savol qo\'shish uchun /question bosing \n"
                                 f"Javoblar jadvalini yuklash uchun /statistic bosing"
                                 )
        else:
            await commands.add_user(user_id=message.from_user.id,
                                    full_name=message.from_user.full_name,
                                    address="", phone="", is_admin=True)
            await message.answer(f"Hush kelibsiz, admin \n"
                                 f"Yangi savol qo\'shish uchun /question bosing \n"
                                 f"Javoblar jadvalini yuklash uchun /statistic bosing")
    else:
        await message.answer("Parol noto'g'ri")
    await state.finish()
