import pymysql
import pygame
import constants


class Database:
    def __init__(self):
        self.a = 1
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='Andres5354317',
            db='triqui'
        )
        self.cursor = self.connection.cursor()

    def saveName(self, name):
        insertName = f"INSERT INTO jugador(nombre) values ('{name}');"

        try:
            self.cursor.execute(insertName)
            self.connection.commit()
        except Exception as e:
            raise

    def saveScore(self, score, name):
        insertScore = f"INSERT INTO puntaje SET puntaje = {score}, id_jugador= ( SELECT id_jugador FROM jugador WHERE nombre='{name}');"
        try:
            self.cursor.execute(insertScore)
            self.connection.commit()
        except Exception as e:
            raise

    def scores(self):
        pass


class Player:
    def __init__(self):
        self.score = 0
        self.name = ''

    def win(self):
        self.score += 1

    def saveScore(self):
        print(self.score, self.name)
        database = Database()
        database.saveName(self.name)
        database.saveScore(self.score, self.name)
