from models import db_api


async def add_new_accounts(accounts: list[str]):
    await db_api.add_accounts(accounts)


