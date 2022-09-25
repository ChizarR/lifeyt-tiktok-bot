import os
import dotenv


dotenv.load_dotenv()


class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    PATH_TO_CHROME_DRIVER = os.getenv("PATH_TO_CHROME_DRIVER", "")
