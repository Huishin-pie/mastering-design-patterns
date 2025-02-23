from typing import List


from video.video import Video
from observer.channel_observer import channelObserver


class Channel():

    def __init__(self, name: str):
        self.name = name
        self.videos: List[Video] = []
        self.observers :List[channelObserver] = []

    def upload(self, video: Video):
        self.videos.append(video)
        print(f"頻道 {self.name} 上架了一則新影片 \"{video.title}\"")
        self.notify()

    def notify(self):
        for observer in self.observers:
            observer.update(self.name)

    def subscribe(self, observer: channelObserver):
        self.observers.append(observer)
        observer.channels.append(self)
        print(f"{observer.name} 訂閱了 {self.name}")

    def unsubscribe(self, observer: channelObserver):
        if observer in self.observers:
            self.observers.remove(observer)
            observer.channels.remove(self)
            print(f"{observer.name} 解除訂閱了 {self.name}")