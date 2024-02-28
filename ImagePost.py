from matplotlib import pyplot as plt, image as mpimg

from AbstractPost import AbstractPost

from NotificationManager import NotificationManager
from Notification import Notification

class ImagePost(AbstractPost):

    def __init__(self, user, filePath):
        super().__init__(user)
        self.__user = user
        self.__filePath = filePath
        print(self)

    def display(self):
        print("Shows picture")
        plt.imshow(mpimg.imread(self.__filePath))
        plt.axis("off")
        plt.show()

    def __str__(self):
        return "{} posted a picture\n".format(self.__user.get_username())
