from dotenv import load_dotenv
import os
import sys
import mysql.connector
from mysql.connector import pooling


class Connection:

    load_dotenv(os.getcwd() + "/../../.env.gorest")
    user = os.getenv('ADMIN')
    password = os.getenv('PASSWORD')
    host = os.getenv('HOST')
    database = os.getenv('DATABASE')

    __DATABASE = database
    __USERNAME = user
    __PASSWORD = password
    __HOST = host
    __POOL_NAME = 'pynative_pool'
    __POOL_SIZE = 3
    __POOL_RESET_SESSION = True

    @classmethod
    def get_pool(cls):
        if cls.__connection_pool is None:
            try:
                cls.__connection_pool = mysql.connector.pooling.MySQLConnectionPool(cls.__POOL_SIZE,
                                                                                    cls.__POOL_RESET_SESSION,
                                                                                    cls.__POOL_NAME,
                                                                                    host=cls.__HOST,
                                                                                    user=cls.__USERNAME,
                                                                                    password=cls.__PASSWORD,
                                                                                    database=cls.__DATABASE
                                                                                    )

                logger.debug(f'Successful pool creation: {cls.__connection_pool}')
                return cls.__connection_pool

            except Exception as e:
                logger.error(f'Error when creating connection pool: {e}')
                sys.exit()
        else:
            return cls.__connection_pool

    @classmethod
    def get_pool_connection(cls):
        connect = cls.get_pool().get_connection()
        logger.debug(f'Connection obtained from the pool: {connect}')
        return connect

    @classmethod
    def free_pool_connection(cls, connect):
        cls.get_pool().putconn(connect)
        logger.debug(f'Return connection to the pool')
        logger.debug(f'Status to the Pool: {cls.__pool}')

    @classmethod
    def close_connection(cls):
        cls.get_pool().closeall()
        logger.debug(f'we close all pool connections: {cls.__pool}')


if __name__ == '__main__':
    # Obtener una conexion a partir del pool
    connection = Connection.get_pool_connection()
    connection1 = Connection.get_pool_connection()
    # Regresar conexiones al pool
    Connection.free_pool_connection(connection)
    Connection.free_pool_connection(connection1)
    # Cerramos el pool
    Connection.close_connection()

