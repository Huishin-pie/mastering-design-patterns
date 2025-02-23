import traceback


from channel.channel import Channel
from video.video import Video
from observer.click_like_subscriber import ClickLikeSubscriber
from observer.unsubscribe_subscriber import UnsubscribeSubscriber


def main():
    try:
        pew_channel = Channel("PewDiePie")
        water_ball_channel = Channel("水球軟體學院")

        water_subscriber = ClickLikeSubscriber("水球")
        fire_subscriber = UnsubscribeSubscriber("火球")

        water_ball_channel.subscribe(water_subscriber)
        pew_channel.subscribe(water_subscriber)

        water_ball_channel.subscribe(fire_subscriber)
        pew_channel.subscribe(fire_subscriber)

        water_ball_channel.upload(Video("C1M1S2", "這個世界正是物件導向的呢！", 240))
        pew_channel.upload(Video("Hello guys", "Clickbait", 30))
        water_ball_channel.upload(Video("C1M1S3", "物件 vs. 類別", 60))
        pew_channel.upload(Video("Minecraft", "Let’s play Minecraft", 1800))

    except Exception as e: 
        traceback.print_exc()

if __name__ == "__main__":
    main()