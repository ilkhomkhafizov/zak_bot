import os
from aiogram import types
from aiogram.types import InputFile

from loader import dp
from filters import IsPrivate
from utils.check_admin import check_admin
from utils.db_api import register_commands as commands
import pandas as pd


@dp.message_handler(IsPrivate(), text='/statistic')
@check_admin
async def statistic_command(message: types.Message):
    users = await commands.select_all_users()
    users_arr = []
    for user in users:
        users_arr.append({
            "fio": user.full_name,
            "manzil": user.address,
            "tel_raqami": user.phone,
            "javoblar": user.answer,
            "registrasiya_vaqti": user.created_at,
            "javob_berish_vaqti": user.updated_at,
        })
    df = pd.DataFrame(data=users_arr)
    df["registrasiya_vaqti"] = df['registrasiya_vaqti'].apply(lambda a: pd.to_datetime(a).
                                                              tz_convert('Asia/Tashkent').isoformat())
    df["javob_berish_vaqti"] = df['javob_berish_vaqti'].apply(lambda a: pd.to_datetime(a).
                                                              tz_convert('Asia/Tashkent').isoformat())
    df.to_excel('statistics.xlsx', index=False)
    excel_bytes = InputFile(path_or_bytesio='statistics.xlsx')
    await dp.bot.send_document(chat_id=message.chat.id,
                               document=excel_bytes)
