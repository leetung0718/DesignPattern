"""
Behavioral Pattern - Observer(PubSub) 觀察者模式
定義物件之間的一種一對多的依賴關係，當一個物件發生改變的時候，所有依賴於他的物件都得到通知並被自動更新。
"""

from abc import ABC, abstractclassmethod


class YoutubeChannel:
    def __init__(self, name):
        self.name = name
        self.subscribers = []

    def subscribe(self, sub):
        self.subscribers.append(sub)

    def notify(self, event):
        for sub in self.subscribers:
            sub.sendNotification(self.name, event)


class YoutubeSubscriber(ABC):
    @abstractclassmethod
    def sendNotification(self, event):
        pass


class YoutubeUser(YoutubeSubscriber):
    def __init__(self, name):
        self.name = name

    def sendNotification(self, channel, event):
        print(f"User {self.name} received notification from {channel}: {event}")


channel1 = YoutubeChannel("neetcode")
channel1.subscribe(YoutubeUser("sub1"))
channel1.subscribe(YoutubeUser("sub2"))
channel1.subscribe(YoutubeUser("sub3"))

channel1.notify("A new video released.")
