from TextPost import TextPost
from ImagePost import ImagePost
from SalePost import SalePost


class PostFactory:

    @staticmethod
    def create_post(postType, user, *arg):
        if postType == "Text":
            return TextPost(user, arg[0])
        elif postType == "Image":
            return ImagePost(user, arg[0])
        elif postType == "Sale":
            return SalePost(user, arg[0], arg[1], arg[2])
        else:
            raise Exception("Post type doesn't exist!")
