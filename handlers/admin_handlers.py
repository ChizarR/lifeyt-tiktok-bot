from aiogram import types
from handlers import answers

from loader import dp
from services import admin_service
from utils import parser


@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    await msg.answer(answers.start)


@dp.message_handler(commands=["add_accounts"])
async def add_account(msg: types.Message):
    accounts = parser.parse_command(msg.text)
    await admin_service.add_new_accounts(accounts)
    await msg.answer("Okey")
