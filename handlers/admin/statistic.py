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
            "full_name": user.full_name,
            "address": user.address,
            "phone": user.phone,
            "answer": user.answer,
            "created_at": user.created_at,
            "updated_at": user.updated_at,
        })
    df = pd.DataFrame(data=users_arr)
    df["created_at"] = df['created_at'].apply(lambda a: pd.to_datetime(a).tz_convert('Asia/Tashkent').isoformat())
    df["updated_at"] = df['updated_at'].apply(lambda a: pd.to_datetime(a).tz_convert('Asia/Tashkent').isoformat())
    df.to_excel('statistics.xlsx', index=False)
    excel_bytes = InputFile(path_or_bytesio='statistics.xlsx')
    await dp.bot.send_document(chat_id=message.chat.id,
                               document=excel_bytes)
