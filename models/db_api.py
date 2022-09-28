from tiktok_api.utils.my_types import VideoInfo

from .account import Account
from .channel import Channel
from .video import Video
from utils import parser


# Videos
async def get_last_saved_link():
    last_video = await Video.all().order_by("-id").first()
    if last_video == None:
        return None
    link = last_video.tiktok_link
    return link


async def add_video(video_info: VideoInfo):
    await Video.get_or_create(
        tiktok_link=video_info.tiktok_link,
        link_to_download=video_info.source_link,
        account=video_info.account
    )


async def get_video(link: str):
    video = await Video.get_or_none(tiktok_link=link)
    return video


# Accounts
async def add_accounts(accounts: list):
    for account in accounts:
        account = parser.parse_account(account)
        await Account.get_or_create(
            account=account
        )


async def get_all_accounts():
    raw_accounts = await Account.all()
    accounts = []
    for raw_acc in raw_accounts:
        accounts.append(raw_acc.account)
    return accounts


# Channels
async def get_all_channels():
    channels_ids = []
    channels = await Channel.all()
    for channel in channels:
        channels_ids.append(channel.channel_id)
    return channels_ids
