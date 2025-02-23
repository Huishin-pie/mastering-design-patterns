from abc import ABC, abstractmethod


class channelObserver(ABC):

    @abstractmethod
    def update(self, channel_name: str):
        pass