from matplotlib import pyplot as plt, image as mpimg

from AbstractPost import AbstractPost

from NotificationManager import NotificationManager
from Notification import Notification

class ImagePost(AbstractPost):

    def __init__(self, user, filePath):
        self.__user = user
        self.__filePath = filePath
        print(self)

    def display(self):
        print("Shows picture")
        plt.imshow(mpimg.imread(self.__filePath))
        plt.axis("off")
        plt.show()

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
        return "{} posted a picture\n".format(self.__user.get_username())
