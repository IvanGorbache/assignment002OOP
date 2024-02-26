

class NotificationManager:
    subscriptions = {}

    @staticmethod
    def subscribe(subscriber, notification):
        if subscriber not in NotificationManager.subscriptions:
            NotificationManager.subscriptions[subscriber] = []
        if subscriber != notification.get_sender():
            NotificationManager.subscriptions[subscriber].append(notification)

    @staticmethod
    def unsubscribe(subscriber, userToUnsubscribeFrom):
        if subscriber in NotificationManager.subscriptions:
            for subscription in NotificationManager.subscriptions[subscriber]:
                if subscription.get_sender() == userToUnsubscribeFrom:
                    NotificationManager.subscriptions[subscriber].remove(subscription)

    @staticmethod
    def notify(subscriber):
        print("{}'s notifications:".format(subscriber.get_username()))
        if subscriber in NotificationManager.subscriptions:
            for notification in NotificationManager.subscriptions[subscriber]:
                print(notification.get_message())

