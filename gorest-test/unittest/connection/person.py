from logger import logger


class Persons:
    def __init__(self, id_post=None, id_user=None, name=None, email=None, gender=None, status=None, date=None):
        self.__id_post = id_post
        self.__id_user = id_user
        self.__name = name
        self.__email = email
        self.__gender = gender
        self.__status = status
        self.__date = date

    def __str__(self):
        return (
            f'id_post: {self.__id_post}, '
            f'id_user: {self.__id_user}, '
            f'name: {self.__name}, '
            f'email: {self.__email}, '
            f'gender: {self.__gender}, '
            f'status: {self.__status}, '
            f'date: {self.__date}'
        )

    @property
    def id_post(self):
        return self.__id_post

    @id_post.setter
    def id_post(self, id_post):
        self.__id_post = id_post

    @property
    def id_user(self):
        return self.__id_user

    @id_user.setter
    def id_user(self, id_user):
        self.id_user = id_user

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        self.__gender = gender

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.status = status

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date


if __name__ == '__main__':
    persona1 = Persons(1, 'Juan', 'Perez', 'email')
    logger.debug(persona1)
    # simulando un objeto a insertar de tipo persona
    persona2 = Persons()
    logger.debug(persona2)
    # simular el caso de eliminar un objeto de tipo persona
    persona3 = Persons(id_person=1)
    logger.debug(persona3)
