from aiogram import Dispatcher, executor

from loader import scheduler
from models import db
from services import tt_api_service


async def on_startup(_: Dispatcher):
    try:
        print("[INFO] [CONNECTED TO DB]")
        await db.open_db_connection()
    except Exception as ex:
        print(ex)

    scheduler.add_job(tt_api_service.watch_new_videos, 
                      "interval", minutes=5)
    scheduler.start()
    print("[INFO] [STARTED SCHEDULER]")



async def on_shutdown(_: Dispatcher):
    await db.close_db_connection()
    print("[INFO] [DB CONNECTION CLOSED]")
    scheduler.shutdown()
    print("[INFO] [SCHEDULER SHUTTED DOWN]")


if __name__ == "__main__":
    from handlers import dp
    executor.start_polling(
        dp, skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown
    )
