# Problem Statement:
# Create a base class Notification with a method send(). Derive EmailNotification,
# SMSNotification, and PushNotification. Override send() to display the appropriate
# notification method.

class Notification:
    def send(self):
        pass


class EmailNotification(Notification):
    def send(self):
        print("Sending Email notification")


class SMSNotification(Notification):
    def send(self):
        print("Sending SMS notification")


class PushNotification(Notification):
    def send(self):
        print("Sending Push notification")


notifications = [EmailNotification(), SMSNotification(), PushNotification()]

for notification in notifications:
    notification.send()
