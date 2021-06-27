import sys
import pymysql


class Database:
    def __init__(self):
        self.a = 1
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='Andres5354317',
            db='jugador'
        )
        self.cursor = self.connection.cursor()
        print("conexión establecida")


database = Database()
