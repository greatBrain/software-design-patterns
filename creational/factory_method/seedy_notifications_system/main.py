from factories.notification_factory import NotificationFactory

def main():
    notification_type = input("Write your prefered method for sending you the confirmation message: sms, email, push \n")
    message = input("Message:").strip()

    try:
        notification = NotificationFactory.create_notification(notification_type)
        notification.send(message)

    except:
        raise ValueError

    finally:
        return True


if __name__ == "__main__":
   main()
