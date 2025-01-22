''' Imagine we are building a system that sends notifications to users. 
We want to support different types of notifications such as Email, SMS, and Push Notifications. 
We will use the Strategy pattern to allow changing the notification type flexibly.'''

from abc import ABC, abstractmethod

class NotificationStrategy(ABC):
      @abstractmethod 
      def send_notification(self):
          pass


class EmailNotification(NotificationStrategy):
    def send_notification(self, message: str):
        return message


class SMSNotification(NotificationStrategy):
    def send(self, message: str):
        return message


class PushNotification(NotificationStrategy):
    def send(self, message: str):
        return message


class NotificationSender:
      def __init__(self, strategy: NotificationStrategy):
          self.strategy = strategy

      def set_strategy(self, strategy: NotificationStrategy):
          self.strategy = strategy

      def notify(self, message: str):
          self.strategy.send(message)



email_strategy = EmailNotification()
sms_strategy = SMSNotification()
push_strategy = PushNotification()

sender = NotificationSender(email_strategy)

sender.notify("Welcome to our service!")

sender.set_strategy(sms_strategy)
sender.notify("Your code is 1234")

sender.set_strategy(push_strategy)
sender.notify("You have a new message!")
