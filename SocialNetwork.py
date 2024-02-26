from User import User


class SocialNetwork:
    __instance = None

    @staticmethod
    def get_instance(name):
        if SocialNetwork.__instance is None:
            SocialNetwork(name)

    def __init__(self, name):
        self.name = name
        self.users = {}
        SocialNetwork.__instance = self
        print("The social network {} was created!".format(name))

    def sign_up(self, username, password):
        if username not in self.users and 4 < len(password) < 8:
            self.users[username] = User(username, password)
            return self.users[username]

    def log_in(self, username, password):
        if username in self.users and password == self.users[username].get_password():
            print(self.users[username].get_username(), "connected")
            self.users[username].go_online()

    def log_out(self, username):
        if username in self.users:
            print(self.users[username].get_username(), "disconnected")
            self.users[username].go_offline()

    def __str__(self):
        description = "{} social network:".format(self.name)
        for username in self.users:
            description += "\n"+self.users[username].__str__()
        return description + "\n"

