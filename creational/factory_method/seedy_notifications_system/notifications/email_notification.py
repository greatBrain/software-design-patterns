from .notification import INotification

class EmailNotification(INotification):

      def send(self, message: str) -> None:
          print("Sending message by email: {}".format(message))