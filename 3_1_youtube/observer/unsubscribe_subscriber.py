from typing import List


from .channel_observer import channelObserver
from channel.channel import Channel


class UnsubscribeSubscriber(channelObserver):

    def __init__(self, name: str):
        self.name = name
        self.channels: List[Channel] = []

    def update(self, channel_name: str):
        channel = next((c for c in self.channels if c.name == channel_name), None)
    
        if channel and channel.videos:
            video = channel.videos[-1]

            if video.length <= 60:
                channel.unsubscribe(self)