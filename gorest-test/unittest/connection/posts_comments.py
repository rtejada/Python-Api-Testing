
class PostsComment:
    def __init__(self, id=None, post_id=None, name=None, email=None, body=None, date=None):

        self.__id = id
        self.__post_id = post_id
        self.__name = name
        self.__email = email
        self.__body = body
        self.__date = date

    def __str__(self):
        return (
            f'id: {self.__id}, '
            f'id_post: {self.__post_id}, '
            f'name: {self.__name}, '
            f'email: {self.__email},'
            f'body: {self.__body}, '                 
            f'date: {self.__date}'
        )

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def post_id(self):
        return self.__post_id

    @post_id.setter
    def post_id(self, post_id):
        self.__post_id = post_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

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