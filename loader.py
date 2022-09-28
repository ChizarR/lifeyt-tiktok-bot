from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from tiktok_api import TikTokAPI

from config import Config


bot = Bot(Config.BOT_TOKEN)
dp = Dispatcher(bot)

tiktok = TikTokAPI(Config.PATH_TO_CHROME_DRIVER)
scheduler = AsyncIOScheduler()
