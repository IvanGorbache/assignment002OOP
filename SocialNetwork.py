from User import User


class SocialNetwork:
    __instance = None

    @staticmethod
    def get_instance(name):
        if SocialNetwork.__instance is None:
            SocialNetwork(name)

    def __init__(self, name):
        if SocialNetwork.__instance is not None:
            raise Exception("Exception: Network already exists!")
        self.name = name
        self.users = {}
        SocialNetwork.__instance = self
        print("The social network {} was created!".format(name))

    def sign_up(self, username, password):
        if username not in self.users:
            if 4 < len(password) < 8:
                self.users[username] = User(username, password, self)
                return self.users[username]
            else:
                raise Exception("Password must be between 4 to 8 characters")
        else:
            raise Exception("User already exists!")

    def log_in(self, username, password):
        if username in self.users and password == self.users[username].get_password() and not self.users[username].is_online():
            print(self.users[username].get_username(), "connected")
            self.users[username].go_online()

    def log_out(self, username):
        if username in self.users and self.users[username].is_online():
            print(self.users[username].get_username(), "disconnected")
            self.users[username].go_offline()

    def does_user_exist(self, username):
        return username in self.users

    def __str__(self):
        description = "{} social network:".format(self.name)
        for username in self.users:
            description += "\n"+self.users[username].__str__()
        return description + "\n"

