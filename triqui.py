import pygame
from board import Board
from button import Button
import constants

pygame.init()
screen = pygame.display.set_mode(constants.SIZE)
pygame.display.set_caption("Triqui")

board = Board()


player = 1

newGameButton = Button(
    "Nuevo juego",
    (400, 400),
    font=50,
    bg="white")
restartButton = Button(
    "Revancha",
    (300, 400),
    font=50,
    bg="white")
menuButton = Button(
    "menu",
    (500, 400),
    font=50,
    bg="white")


# principal loop
menu = True
buttons = False
wait = True
playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if not menu:
            if not buttons:
                board.lines(screen)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    row = mouse[1]//300
                    col = mouse[0]//300
                    if board.isValidSquare(row, col):
                        if player == 1:
                            board.squareIsSelected(row, col, 1)
                            if board.win(player):
                                buttons = True
                            player = 2
                        else:
                            board.squareIsSelected(row, col, 2)
                            if board.win(player):
                                buttons = True
                            player = 1
                        board.figures(screen)
                        if board.boardFull():
                            buttons = True
            else:
                if wait:
                    pygame.time.wait(1000)
                    wait = False
                board.restart(screen)
                restartButton.show(screen)
                menuButton.show(screen)
                if restartButton.click(event):
                    screen.fill(pygame.Color('black'))
                    buttons = False
                    menu = False
                    wait = True
                    player = 1
                if menuButton.click(event):
                    screen.fill(pygame.Color('black'))
                    menu = True
                    wait = True
                    player = 1
        else:
            newGameButton.show(screen)
            if newGameButton.click(event):
                screen.fill(pygame.Color('black'))
                menu = False
                buttons = False

    pygame.display.update()
