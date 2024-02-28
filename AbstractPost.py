from abc import ABC, abstractmethod

from Notification import Notification
from NotificationManager import NotificationManager


class AbstractPost(ABC):

    def __init__(self, user):
        self.__user = user
        self.__comments = []
        self.__likes = []

    def comment(self, user, newComment):
        if user is not self.__user:
            NotificationManager.subscribe(self.__user,
                                          Notification(user, self.__user,
                                                       "{} commented on your post".format(user.get_username())))
        print(
            "notification to {}: {} commented on your post: {}".format(self.__user.get_username(), user.get_username(),
                                                                       newComment))
        self.__comments.append("{} commented on {}'s post: {}".format(self.__user.get_username(), user, newComment))

    def like(self, user):

        if user not in self.__likes:
            if user is not self.__user:
                NotificationManager.subscribe(self.__user, Notification(user, self.__user,
                                                                        "{} liked your post".format(user.get_username())))
                print("notification to {}: {} liked your post".format(self.__user.get_username(), user.get_username()))
            self.__likes.append(user)
        else:
            raise Exception("User already liked this")

    def print_comments(self):
        for comment in self.__comments:
            print(comment)

    @abstractmethod
    def __str__(self):
        pass
