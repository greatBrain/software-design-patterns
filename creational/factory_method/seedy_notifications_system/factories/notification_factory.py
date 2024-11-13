from notifications.email_notification import EmailNotification
from notifications.sms_notification import SMSNotification
from notifications.push_notification import PushNotification

class NotificationFactory:

      @staticmethod
      def create_notification(notification_type: str):
          notifications_map = {
            "email": EmailNotification(),
            "sms": SMSNotification(),
            "push": PushNotification()
          }

          notification_instance = notifications_map.get(notification_type.lower())

          if not notification_instance:
             raise ValueError("Unknown notification type: {}".format(notification_type))
          
          return notification_instance