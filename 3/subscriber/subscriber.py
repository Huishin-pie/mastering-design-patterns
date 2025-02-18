from typing import List


from .channel_observer import channelObserver
from channel.channel import Channel
from action.action_strategy import ActionStrategy


class Subscriber(channelObserver):

    def __init__(self, name: str, action: ActionStrategy):
        self.name = name
        self.action = action
        self.channels :List[Channel] = []

    def update(self, channel_name: str):
        channel = next((c for c in self.channels if c.name == channel_name), None)
    
        if channel and channel.videos:
            video = channel.videos[-1]
            self.action.action(channel, video, self.name)

    def subscribe(self, channel: Channel):
        self.channels.append(channel)
        channel.register(self)
        print(f"{self.name} 訂閱了 {channel.name}")

    def unsubscribe(self, channel: Channel):
        self.channels.remove(channel)
        channel.unregister(self)
        print(f"{self.name} 解除訂閱了 {channel.name}")