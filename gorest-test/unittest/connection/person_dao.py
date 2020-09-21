from person import Persons
from connect_database import Connection
from logger import logger
from connection.dao_base import DaoBase


class PersonDao(DaoBase):

    __SELECT = 'SELECT * FROM persons ORDER BY id_user'
    __INSERT = 'INSERT INTO persons(id_user, name, email, gender, status, date) VALUES(%s,%s,%s,%s,%s,%s)'
    __DELETE = 'DELETE FROM persons WHERE id_user = %s'

    @classmethod
    def select(cls):
        cursor = Connection.get_cursor()
        logger.debug(cursor.mogrify(cls.__SELECT))
        cursor.execute(cls.__SELECT)
        registers = cursor.fetchall()

        people = []
        for register in registers:
            person = Persons(register[0], register[1], register[2], register[3], register[4], register[5], register[6])
            people.append(person)
        Connection.close()
        return people
