from PostFactory import PostFactory
from NotificationManager import NotificationManager
from Notification import Notification

class User(object):
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__posts = []
        self.__followers = []
        self.__online = True

    def follow(self, userToFollow):
        userToFollow.add_follower(self)

    def add_follower(self, follower):
        if follower not in self.__followers:
            print("{} started following {}".format(follower.get_username(), self.__username))
            self.__followers.append(follower)

    def unfollow(self, userToUnfollow):
        NotificationManager.unsubscribe(self, userToUnfollow)
        userToUnfollow.remove_follower(self)

    def remove_follower(self, userToRemove):
        if userToRemove in self.__followers:
            print("{} unfollowed {}".format(userToRemove.get_username(), self.__username))
            self.__followers.remove(userToRemove)

    def publish_post(self, postType, *arg):
        if self.__online:
            for follower in self.__followers:
                NotificationManager.subscribe(follower, Notification(self, follower, "{} has a new post".format(self.__username)))
            new_post = PostFactory.create_post(postType, self, *arg)
            self.__posts.append(new_post)
            return new_post

    def go_online(self):
        self.__online = True

    def go_offline(self):
        self.__online = False

    def print_notifications(self):
        NotificationManager.notify(self)

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_posts(self):
        return self.__posts

    def get_followers(self):
        return self.__followers

    def __str__(self):
        return "User name: {}, Number of posts: {}, Number of followers: {}".format(self.__username, len(self.__posts), len(self.__followers))
