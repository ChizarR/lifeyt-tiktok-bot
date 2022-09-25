from aiogram import types
from handlers import answers

from loader import dp


@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    await msg.answer(answers.start)


@dp.message_handler(command=["add_account"])
async def add_account(msg: types.Message):
    pass
