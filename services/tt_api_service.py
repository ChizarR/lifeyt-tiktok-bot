from tiktok_api.utils.my_types import VideoInfo

from loader import tiktok


def get_new_videos_from_account(account: str, old_links: list) -> list[str]:
    links = tiktok.fetch_account_links(account)
    links.reverse()
    new_video_links = []

    for video_link in links:
        if video_link in old_links:
            break
        new_video_links.append(video_link)

    return new_video_links


def download_videos(video_links: list) -> list[VideoInfo]:
    video_cards = []

    for video_link in video_links:
        video_info = tiktok.get_video(video_link)
        video_cards.append(video_info)

    return video_cards
