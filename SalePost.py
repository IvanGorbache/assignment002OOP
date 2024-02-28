from AbstractPost import AbstractPost
from NotificationManager import NotificationManager
from Notification import Notification

class SalePost(AbstractPost):

    def __init__(self, user, item, price, location):
        super().__init__(user)
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

    def __str__(self):
        return "{} posted a product for sale:\n{} {}, price: {}, pickup from: {}\n".format(self.__user.get_username(),"Sold!" if self.__is_sold else "For sale!", self.__item, self.__price, self.__location)
