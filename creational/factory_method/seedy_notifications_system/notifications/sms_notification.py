from .notification import INotification

class SMSNotification(INotification):

      def send(self, message: str) -> None:
          print("Sending message to SMS: {}".format(message))