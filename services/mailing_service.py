import asyncio
import os
from aiogram import Dispatcher
from tiktok_api.utils.my_types import VideoInfo

from config import Config
from models import db_api


async def send_videos_to_channels(dp: Dispatcher, 
                                  video_cards: list[VideoInfo]):
    for card in video_cards:
        await asyncio.sleep(0.5)
        path_to_video = card.path_to_saved_video
        video = open(path_to_video, "rb")

        account = card.account
        likes = card.like_count
        shares = card.share_count
        comments = card.comment_count
        link = card.tiktok_link
        
        await dp.bot.send_video(
            chat_id=Config.CHANNEL_ID,
            video=video,
            caption=_generate_text(
                account, likes, shares, comments, link
            )
        )

        os.remove(path_to_video)
    

def _generate_text(*args):
    answer = f"Acc: {args[0]}\nLikes: {args[1]}\nShares: {args[2]}\nComments: {args[3]}\nLink: {args[4]}"
    return answer
