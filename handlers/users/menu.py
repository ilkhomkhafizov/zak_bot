from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

javob = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=f'Javobni kiriting!')
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
