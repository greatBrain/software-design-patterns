from abc import ABC, abstractmethod

class Notification(ABC):      
      @abstractmethod
      def send_message(self):
          pass


class BasicNotification(Notification):      
      def send_message(self, message):
          return "Message{}".format(message)


class NotificationDecorator(Notification):
      def __init__(self, notification:Notification):
          self._notification = notification

      def send_message(self):
          pass
