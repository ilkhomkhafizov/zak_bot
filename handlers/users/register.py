from aiogram import types
from aiogram.dispatcher import FSMContext

from filters import IsPrivate
from .menu import javob
from loader import dp
from states import User
from utils.db_api import register_commands


@dp.message_handler(IsPrivate(), text='Ro\'yhatdan o\'tish')
async def register_command(message: types.Message):
    user = await register_commands.select_user_by_id(user_id=message.from_user.id)
    if user:
        await message.answer("Siz registrasiya bo'lgansiz")
    else:
        text = f'Zakovat ishtirokchisining ismi, \n' \
               f'familiyasi va otasining ismi:'
        await message.answer(text)
        await User.full_name.set()


@dp.message_handler(IsPrivate(), state=User.full_name)
async def fio_command(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(full_name=answer)
    text = f'Zakovat ishtirokchisining turar joy manzili: \n '
    await message.answer(text)
    await User.address.set()


@dp.message_handler(IsPrivate(), state=User.address)
async def address_command(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(address=answer)
    text = f'Zakovat ishtirokchisining telefon raqami:'
    await message.answer(text)
    await User.phone.set()


@dp.message_handler(IsPrivate(), state=User.phone)
async def phone_command(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(phone=answer)
    text = f'Siz qoldirgan ma’lumotlar qabul qilindi. \n ' \
           f'Zakovat intellektual o\'yinlarida ishtirokingiz uchun minnatdorchilik bildiramiz!'
    data = await state.get_data()
    full_name = data.get('full_name')
    address = data.get('address')
    phone = data.get('phone')
    await register_commands.add_user(user_id=message.from_user.id, full_name=full_name,
                                     address=address, phone=phone)

    await state.finish()
    await message.answer(text, reply_markup=javob)
