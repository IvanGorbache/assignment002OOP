from abc import ABC, abstractmethod


class AbstractPost(ABC):

    @abstractmethod
    def comment(self, user, newComment):
        pass

    @abstractmethod
    def like(self, user):
        pass

    @abstractmethod
    def __str__(self):
        pass
