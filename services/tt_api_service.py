from aiogram import Dispatcher
from tiktok_api.utils.my_types import VideoInfo

from loader import tiktok
from models import db_api
from services import mailing_service


async def watch_account(account: str):
    links = tiktok.fetch_account_links(account)

    list_to_download = await _create_list_to_download(links)
    video_cards = await _download_videos(list_to_download)
    return video_cards


async def _create_list_to_download(links: list[str]) -> list[str] | None:
    links.reverse()

    new_links = []
    for link in links:
        video = await db_api.get_video(link)
        if video is None:
            new_links.append(link)
        else:
            continue

    return new_links


async def _download_videos(video_links: list[str] | None) -> list[VideoInfo] | None:
    if video_links == None:
        return None

    video_cards = []
    for video_link in video_links:
        try:
            video_info = tiktok.get_video(video_link)
            video_cards.append(video_info)
            await db_api.add_video(video_info)
        except IndexError:
            print(f"Link {video_link} is not avaliable...")
            continue

    return video_cards


async def watch_new_videos():
    print("----------- TEST -----------")
    all_accounts = await db_api.get_all_accounts()

    for account in all_accounts:
        new_videos = await watch_account(account)
        if new_videos == None:
            continue
        dp = Dispatcher.get_current()
        await mailing_service.send_videos_to_channels(dp, new_videos)

