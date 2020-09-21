from posts import Posts
from connect_database import Connection
from logger import logger
from connection.dao_base import DaoBase


class PostDao(DaoBase):

    __SELECT = 'SELECT * FROM posts ORDER BY user_id'
    __INSERT = 'INSERT INTO persons(id_user, name, email, gender, status, date) VALUES(%s,%s,%s,%s,%s,%s)'
    __DELETE = 'DELETE FROM persons WHERE id_user = %s'

    @classmethod
    def select(cls):
        cursor = Connection.get_cursor()
        logger.debug(cursor.mogrify(cls.__SELECT))
        cursor.execute(cls.__SELECT)
        registers = cursor.fetchall()

        Posts_User = []
        for register in registers:
            post = Posts(register[0], register[1], register[2], register[3], register[4])
            Posts_User.append(post)
        Connection.close()
        return Posts_User
