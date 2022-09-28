from tortoise import fields
from tortoise.models import Model


class Account(Model):
    id = fields.BigIntField(pk=True)
    account = fields.CharField(255, unique=True)

    class Meta:
        table = "accounts"
