from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Ботни ишга тушуриш'),
        types.BotCommand('register', 'Регистрациядан утиш'),
        types.BotCommand('answer', 'Жавоб йуллаш')
    ])
