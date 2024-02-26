from AbstractPost import AbstractPost
from NotificationManager import NotificationManager
from Notification import Notification

class TextPost(AbstractPost):

    def __init__(self, user, text):
        self.__user = user
        self.__text = text
        print(self)

    def comment(self, user, newComment):
        if user is not self.__user:
            NotificationManager.subscribe(self.__user,
                                        Notification(user, self.__user, "{} commented on your post".format(user.get_username())))
        print("notification to {}: {} commented on your post: {}".format(self.__user.get_username(), user.get_username(),newComment))

    def like(self, user):
        if user is not self.__user:
            NotificationManager.subscribe(self.__user, Notification(user, self.__user, "{} liked your post".format(user.get_username())))
            print("notification to {}: {} liked your post".format(self.__user.get_username(),user.get_username()))

    def __str__(self):
        return "{} published a post:\n\"{}\"\n".format(self.__user.get_username(), self.__text)
