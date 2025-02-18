from video.video import Video
from .action_strategy import ActionStrategy
from channel.channel import Channel


class ClickLike(ActionStrategy):

    def action(self, channel: Channel, video: Video, subscriber_name: str):
        if video.length >= 180:
            video.clickLike(subscriber_name)