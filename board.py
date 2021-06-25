import pygame
import numpy as np
import constants


class Board:
    def __init__(self):
        self.board = np.zeros((3, 3))

    def squareIsSelected(self, row, col, player):
        self.board[row][col] = player
        return self.board

    def isValidSquare(self, row, col): return self.board[row][col] == 0

    def boardFull(self, row, col):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == 0:
                    return False
        return True

    def getBoard(self):
        return self.board

    def lines(self, screen):
        # vertical lines
        pygame.draw.line(screen, constants.WHITE, (300, 0),
                         (300, 900), constants.LINEWIDTH)
        pygame.draw.line(screen, constants.WHITE, (600, 0),
                         (600, 900), constants.LINEWIDTH)
        # Horizontal lines
        pygame.draw.line(screen, constants.WHITE, (0, 300),
                         (900, 300), constants.LINEWIDTH)
        pygame.draw.line(screen, constants.WHITE, (0, 600),
                         (900, 600), constants.LINEWIDTH)

    def figures(self, screen):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == 1:
                    pygame.draw.circle(
                        screen, constants.WHITE, (col*300+150, row*300+150), constants.CRADIUS, constants.CWIDTH)
                elif self.board[row][col] == 2:
                    pygame.draw.line(screen, constants.WHITE, (col*300+50, row*300+250),
                                     (col*300+250, row*300+50), constants.LINEWIDTH)
                    pygame.draw.line(screen, constants.WHITE, (col*300+50, row*300+50),
                                     (col*300+250, row*300+250), constants.LINEWIDTH)

    def win(self, player):
        # veertical win
        for col in range(3):
            if self.board[0][col] == player and self.board[1][col] == player and self.board[1][col] == player:
                return True
        # horizontal win
        for row in range(3):
            if self.board[row][0] == player and self.board[row][1] == player and self.board[row][2] == player:
                return True
        if self.board[2][0] == player and self.board[1][1] == player and self.board[0][2] == player:
            return True
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True

    def a(self):
        return self.board
