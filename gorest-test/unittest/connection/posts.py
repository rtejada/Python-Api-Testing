
class Posts:
    def __init__(self, post_id=None, user_id=None, title=None, body=None, date=None):
        self.__post_id = post_id
        self.__user_id = user_id
        self.__title = title
        self.__body = body
        self.__date = date

    def __str__(self):
        return (
            f'id_post: {self.__post_id}, '
            f'user_id: {self.__user_id}, '
            f'title: {self.__title},'
            f'body: {self.__body}, '                 
            f'date: {self.__date}'
        )

    @property
    def post_id(self):
        return self.__post_id

    @post_id.setter
    def post_id(self, post_id):
        self.__post_id = post_id

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body):
        self.__body = body

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date


if __name__ == '__main__':
    pass