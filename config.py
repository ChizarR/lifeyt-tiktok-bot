import os
import dotenv


dotenv.load_dotenv()


class Config:
    # Bot
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")

    # Web driver
    PATH_TO_CHROME_DRIVER = os.getenv("PATH_TO_CHROMEDRIVER", "")

    CHANNEL_ID = os.getenv("CHANNEL_ID", "")

    # Postgres DB
    PG_USER = os.getenv("POSTGRES_USER")
    PG_PASS = os.getenv("POSTGRES_PASS")
    PG_HOST = os.getenv("POSTGRES_HOST")
    PG_PORT = os.getenv("POSTGRES_PORT")
    PG_DB_NAME = os.getenv("POSTGRES_DB")
