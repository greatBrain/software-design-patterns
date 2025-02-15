
from abc import ABC, abstractmethod
from typing import List


# To be implemented by followers
class Observer(ABC):      
      @abstractmethod
      def update(self, message: str):
          pass


#Observable subject
class User:
    def __init__(self, name: str):
        self.name = name
        self._followers:List[Observer] = []

    def add_follower(self, follower:Observer):
        if not follower in self._followers:
           self._followers.append(follower)

    def remove_follower(self, follower:Observer):
        try:
           self._followers.remove(follower)
        except Exception as e:
           raise e  

    def post_update(self, message: str):
        print(f"{self.name} posted: {message}")
        self.notify_followers(message)

    def notify_followers(self, message: str):
        for follower in self._followers:
            follower.update(f"{self.name}: {message}")


class Follower(Observer):
    def __init__(self, name: str):
        self.name = name
        
    """Receives a notification when a followed user posts something"""
    def update(self, message: str):
        print("{} received a notification: {}".format(self.name, message))


if __name__=="__main__":
    user1 = User("Alice")
    user2 = User("Bob")

    follower1 = Follower("Charlie")
    follower2 = Follower("David")

    user1.add_follower(follower1)
    user1.add_follower(follower2)
    user2.add_follower(follower1)

    user1.post_update("Hello everyone!\n")
    user2.post_update("Today is a great day.\n")       
