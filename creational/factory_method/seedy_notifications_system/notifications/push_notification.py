from .notification import INotification

class PushNotification(INotification):

      def send(self, message: str) -> None:
          print("Sending message to push: {}".format(message))