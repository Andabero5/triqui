import pygame
import sys
from board import Board
import constants

screen = pygame.display.set_mode(constants.SIZE)
pygame.display.set_caption("Triqui")

board = Board()


player = 1
board.lines(screen)


# principal loop
menu = False
playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            row = mouse[1]//300
            col = mouse[0]//300
            if board.isValidSquare(row, col):
                if player == 1:
                    board.squareIsSelected(row, col, 1)
                    player = 2
                else:
                    board.squareIsSelected(row, col, 2)
                    player = 1
                board.figures(screen)

    pygame.display.update()
