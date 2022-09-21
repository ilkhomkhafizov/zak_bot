from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import dp
from filters import IsPrivate
from utils.misc import rate_limit


@rate_limit(limit=15, key='/start')
@dp.message_handler(IsPrivate(), text='/start')
async def start_command(message: types.Message):
    register = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=f'Ro\'yhatdan o\'tish')
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    text = f'Assalomu alaykum hurmatli bilimdon! \n' \
           f'"Zakovat" intellektual o\'yinlari botiga xush kelibsiz!!! \n' \
           f'Savollarga javob yo\'llashiz uchun, bot orqali registrasiyadan ' \
           f'o\'tishingiz kerak bo\'ladi. Registrasiyadan o\'tish uchun ' \
           f'Ro\'yhatdan o\'tish tugmasini bosing.'
    await message.answer(text, reply_markup=register)


