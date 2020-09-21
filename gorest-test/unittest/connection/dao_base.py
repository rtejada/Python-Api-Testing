from abc import ABC, abstractmethod
from connect_database import Connection
from logger import logger


class DaoBase(ABC):

    def __init__(self, query, value):

        self.query = query
        self.value = value

    @abstractmethod
    def select(self):
        pass

    @classmethod
    def insert(cls, query, values):
        try:
            connection = Connection.get_connected()
            cursor = Connection.get_cursor()
            logger.debug(cursor.mogrify(query))
            cursor.execute(query, values)
            connection.commit()

            return cursor.rowcount

        except Exception as e:
            connection.rollback()
            logger.error(f'Exception to insert person: {e}')

        finally:
            Connection.close()

    @classmethod
    def update(cls, person):
        try:
            connection = Connection.get_connected()
            cursor = Connection.get_cursor()
            logger.debug(cursor.mogrify(cls.__UPDATE))
            logger.debug(f'Person to insert: {person}')
            values = (person.status, person.gender, person.id_user)
            cursor.execute(cls.__UPDATE, values)
            connection.commit()
            return cursor.rowcount

        except Exception as e:
            connection.rollback()
            logger.error(f'Exception to insert person: {e}')

        finally:
            Connection.close()

    @classmethod
    def delete(cls, person):
        try:
            connection = Connection.get_connected()
            cursor = Connection.get_cursor()
            logger.debug(cursor.mogrify(cls.__DELETE))
            logger.debug(f'Person to delete: {person}')
            value = (person.id_user,)
            cursor.execute(cls.__DELETE, value)
            connection.commit()
            return cursor.rowcount

        except Exception as e:
            connection.rollback()
            logger.error(f'Exception to delete person: {e}')

        finally:
            Connection.close()


if __name__ == '__main__':
    # people = PersonDao.select()
    # for person in people:
    # logger.debug(person)
    # logger.debug(person.id_person)

    # person = Person(first_name='Jose', last_name='Castillo', email='jcastillo@mail.com')
    # persons_inserted = PersonDao.insert(person)
    # logger.debug(f'Persons Inserted: {persons_inserted}')

    # person = Person(first_name='Diego', last_name='Suarez', email='dsuarez@mail.com', id_person=18)
    # persons_inserted = PersonDao.update(person)
    # logger.debug(f'Persons Inserted: {persons_inserted}')

    #person = Persons(id_person=18)
    #person_delete = PersonDao.update(person)
    #logger.debug(f'Persons Delete: {person_delete}')

    person =DaoBase.select_one(2)
    print(person)

