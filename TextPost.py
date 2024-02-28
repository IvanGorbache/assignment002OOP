from AbstractPost import AbstractPost
from NotificationManager import NotificationManager
from Notification import Notification

class TextPost(AbstractPost):

    def __init__(self, user, text):
        super().__init__(user)
        self.__user = user
        self.__text = text
        print(self)

    def __str__(self):
        return "{} published a post:\n\"{}\"\n".format(self.__user.get_username(), self.__text)
