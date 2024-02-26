from AbstractPost import AbstractPost
from NotificationManager import NotificationManager
from Notification import Notification

class SalePost(AbstractPost):

    def __init__(self, user, item, price, location):
        self.__user = user
        self.__item = item
        self.__price = price
        self.__location = location
        self.__is_sold = False
        print(self)

    def sold(self, password):
        if self.__is_sold is False and password == self.__user.get_password():
            self.__is_sold = True
            print("{}'s product is sold".format(self.__user.get_username()))

    def discount(self, percent, password):
        if self.__is_sold is False and password == self.__user.get_password():
            self.__price *= ((100 - percent) / 100)
            print("Discount on {} product! the new price is: {}".format(self.__user.get_username(), self.__price))

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
        return "{} posted a product for sale:\n{} {}, price: {}, pickup from: {}\n".format(self.__user.get_username(),"Sold!" if self.__is_sold else "For sale!", self.__item, self.__price, self.__location)
