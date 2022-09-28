from tortoise import fields
from tortoise.models import Model


class Admin(Model):
    id = fields.BigIntField(pk=True)
    tg_id = fields.BigIntField(unique=True)

    class Meta:
        table = "admins"
