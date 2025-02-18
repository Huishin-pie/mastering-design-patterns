import traceback


from channel.channel import Channel
from subscriber.subscriber import Subscriber
from video.video import Video
from action.click_like import ClickLike
from action.unsubscribe import Unsubscribe


def main():
    try:
        pew_channel = Channel("PewDiePie")
        water_ball_channel = Channel("水球軟體學院")

        water_subscriber = Subscriber("水球", ClickLike())
        fire_subscriber = Subscriber("火球", Unsubscribe())

        water_subscriber.subscribe(water_ball_channel)
        water_subscriber.subscribe(pew_channel)

        fire_subscriber.subscribe(water_ball_channel)
        fire_subscriber.subscribe(pew_channel)

        water_ball_channel.upload(Video("C1M1S2", "這個世界正是物件導向的呢！", 240))
        pew_channel.upload(Video("Hello guys", "Clickbait", 30))
        water_ball_channel.upload(Video("C1M1S3", "物件 vs. 類別", 60))
        pew_channel.upload(Video("Minecraft", "Let’s play Minecraft", 1800))

    except Exception as e: 
        traceback.print_exc()

if __name__ == "__main__":
    main()