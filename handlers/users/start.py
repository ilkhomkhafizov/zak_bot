from aiogram import types
from loader import dp
from filters import IsPrivate
from utils.misc import rate_limit


@rate_limit(limit=15, key='/start')
@dp.message_handler(IsPrivate(), text='/start')
async def start_command(message: types.Message):
    text = f'Assalomu alaykum hurmatli bilimdon! \n' \
           f'"Zakovat" intellektual o\'yinlari botiga xush kelibsiz!!! \n' \
           f'Savollarga javob yo\'llashiz uchun, bot orqali registrasiyadan ' \
           f'o\'tishingiz kerak bo\'ladi. Registrasiyadan o\'tish uchun ' \
           f'/register ni bosing.'
    await message.answer(text)


