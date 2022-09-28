from tortoise import Tortoise

from config import Config


__models__ = ["models"]


async def open_db_connection():
    user = Config.PG_USER
    password = Config.PG_PASS
    host = Config.PG_HOST
    port = Config.PG_PORT
    db_name = Config.PG_DB_NAME

    await Tortoise.init(
        db_url=f"postgres://{user}:{password}@{host}:{port}/{db_name}",
        modules={"models": __models__}
    )
    await Tortoise.generate_schemas()


async def close_db_connection():
    await Tortoise.close_connections()
