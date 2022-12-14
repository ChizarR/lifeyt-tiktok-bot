from tortoise import fields
from tortoise.models import Model


class Channel(Model):
    id = fields.BigIntField(pk=True)
    channel_id = fields.BigIntField(unique=True)

    class Meta:
        table = "channels"
