class Notification:
    def __init__(self, sender, recipient, message):
        self.__sender = sender
        self.__recipient = recipient
        self.__message = message

    def get_sender(self):
        return self.__sender

    def get_recipient(self):
        return self.__recipient

    def get_message(self):
        return self.__message
