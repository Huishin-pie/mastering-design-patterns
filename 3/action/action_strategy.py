from abc import ABC, abstractmethod


from video.video import Video
from channel.channel import Channel


class ActionStrategy(ABC):

    @abstractmethod
    def action(self, channel: Channel, video: Video, subscriber_name: str):
        pass