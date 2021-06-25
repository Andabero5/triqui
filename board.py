
import numpy as np


class Board:
    def __init__(self):
        self.board = np.zeros((3, 3))

    def squares(self, row, col, player):
        self.board[row][col] = player
        return self.board

    def isValidSquare(self, row, col): return self.board[row][col] == 0

    def boardFull(self, row, col):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == 0:
                    return False
        return True
