from video.video import Video
from .action_strategy import ActionStrategy
from channel.channel import Channel


class Unsubscribe(ActionStrategy):

    def action(self, channel: Channel, video: Video, subscriber_name: str):
        if video.length <= 60:
            subscriber = next((s for s in channel.observers if s.name == subscriber_name), None)

            if subscriber:
                subscriber.unsubscribe(channel)