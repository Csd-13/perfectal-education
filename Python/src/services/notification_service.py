import datetime

class NotificationService:
    def __init__(self):
        self.notifications = []

    def add_notification(self, content):
        timestamp = datetime.datetime.now()
        self.notifications.append({"content": content, "timestamp": timestamp})

    def get_notifications(self):
        return self.notifications

    def clear_notifications(self):
        self.notifications.clear()
