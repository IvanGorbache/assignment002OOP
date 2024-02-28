from PostFactory import PostFactory
from NotificationManager import NotificationManager
from Notification import Notification


class User(object):
    def __init__(self, username, password, network):
        self.__network = network
        self.__username = username
        self.__password = password
        self.__posts = []
        self.__followers = []
        self.__online = True

    def follow(self, userToFollow):
        if self.__online:
            if self.__network.does_user_exist(userToFollow.get_username()) and self not in userToFollow.get_followers():
                userToFollow.add_follower(self)
            else:
                raise Exception("User already followed!")

    def add_follower(self, follower):
        if self.__network.does_user_exist(follower.get_username()) and follower not in self.__followers:
            print("{} started following {}".format(follower.get_username(), self.__username))
            self.__followers.append(follower)

    def unfollow(self, userToUnfollow):
        if self.__online:
            if self.__network.does_user_exist(userToUnfollow.get_username()) and self in userToUnfollow.get_followers():
                NotificationManager.unsubscribe(self, userToUnfollow)
                userToUnfollow.remove_follower(self)
            else:
                raise Exception("User wasn't followed in the first place!")

    def remove_follower(self, userToRemove):
        if self.__network.does_user_exist(userToRemove.get_username()) and userToRemove in self.__followers:
            print("{} unfollowed {}".format(userToRemove.get_username(), self.__username))
            self.__followers.remove(userToRemove)

    def publish_post(self, postType, *arg):
        if self.__online:
            for follower in self.__followers:
                NotificationManager.subscribe(follower,
                                              Notification(self, follower, "{} has a new post".format(self.__username)))
            new_post = PostFactory.create_post(postType, self, *arg)
            self.__posts.append(new_post)
            return new_post

    def go_online(self):
        self.__online = True

    def go_offline(self):
        self.__online = False

    def print_notifications(self):
        if self.__online:
            NotificationManager.notify(self)

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_posts(self):
        return self.__posts

    def get_followers(self):
        return self.__followers

    def is_online(self):
        return self.__online

    def __str__(self):
        return "User name: {}, Number of posts: {}, Number of followers: {}".format(self.__username, len(self.__posts),
                                                                                    len(self.__followers))
