from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    tg_id = fields.BigIntField(unique=True)
    first_name = fields.CharField(255, null=False)
    username = fields.CharField(255, unique=True) 

    class Meta:
        table = "users"
