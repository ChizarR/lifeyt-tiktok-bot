from tortoise import fields
from tortoise.models import Model


class Video(Model):
    id = fields.BigIntField(pk=True)
    tiktok_link = fields.TextField()
    link_to_download = fields.TextField()
    file_id_tg = fields.BigIntField(null=True)
    account = fields.CharField(200)

    class Meta:
        table = "videos"
    
