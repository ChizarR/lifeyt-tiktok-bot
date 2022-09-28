def parse_command(command: str) -> list:
    return command.split(" ")[1:]


def parse_account(account: str) -> str:
    if account.startswith("@"):
        return account
    else:
        account = "@" + account
        return account
