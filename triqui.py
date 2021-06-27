import pygame
from board import Board
from button import Button, Input
import constants
from player import Player

pygame.init()
screen = pygame.display.set_mode(constants.SIZE)
pygame.display.set_caption("Triqui")

board = Board()
newGameButton = Button(
    "Nuevo juego",
    (320, 380),
    font=50,
    bg="white")
scoreButton = Button(
    "Mejores puntajes",
    (280, 480),
    font=50,
    bg="white")
restartButton = Button(
    "Revancha",
    (510, 425),
    font=50,
    bg="white")
menuButton = Button(
    "Mejores puntajes",
    (510, 425),
    font=50,
    bg="white")


font = pygame.font.SysFont("Corbel", 50)
title = pygame.font.SysFont("Corbel", 90)

player1 = Player()
player2 = Player()
name = Input()


def scoreboard():
    textSurface = font.render(
        f"Puntaje final: {player1.name}: {player1.score} y {player2.name}: {player2.score}", True, constants.WHITE)
    screen.blit(textSurface, (100, 425))
    pygame.display.update()
    pygame.time.wait(3000)
    screen.fill(pygame.Color('black'))


# principal loop
menu = True
buttons = False
wait = True
playing = True
showInputName = False
names = 0
numPlayer = 1
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
                        board.squareIsSelected(row, col, numPlayer)
                        if board.win(numPlayer):
                            if numPlayer == 1:
                                player1.win()
                            elif numPlayer == 2:
                                player2.win()
                            buttons = True
                        numPlayer = numPlayer % 2 + 1
                        if board.boardFull():
                            buttons = True
                        board.figures(screen)

            else:
                if wait:
                    pygame.time.wait(1000)
                    wait = False
                board.restart(screen)
                pygame.draw.line(screen, constants.WHITE,
                                 (450, 0), (450, 900), 1)
                pygame.draw.line(screen, constants.WHITE,
                                 (0, 450), (900, 450), 1)
                textSurface = font.render(
                    f"Puntaje Actual: {player1.name}: {player1.score} y {player2.name}: {player2.score}", True, constants.WHITE)
                screen.blit(textSurface, (100, 300))
                restartButton.show(screen)
                menuButton.show(screen)
                if restartButton.click(event):
                    screen.fill(pygame.Color('black'))
                    buttons = False
                    menu = False
                    wait = True
                    numPlayer = 1
                if menuButton.click(event):
                    screen.fill(pygame.Color('black'))
                    scoreboard()
                    player1.saveScore()
                    player2.saveScore()
                    player1.name = ''
                    player1.score = 0
                    player2.name = ''
                    player2.score = 0
                    menu = True
                    wait = True
                    numPlayer = 1
        else:
            if not showInputName:
                textSurface = title.render(
                    f"TRIQUI", True, constants.WHITE)
                screen.blit(textSurface, (320, 200))
                newGameButton.show(screen)
                scoreButton.show(screen)
                if newGameButton.click(event):
                    screen.fill(pygame.Color('black'))
                    showInputName = True
            elif showInputName:
                name.show(screen, numPlayer+names)
                nameVerified = name.keys(event, screen)
                if nameVerified[1] == True:
                    name.name = ""
                    nameVerified[1] = False
                    screen.fill(pygame.Color('black'))
                    names += 1
                    if names == 1:
                        player1.name = (nameVerified[0])
                    elif names == 2:
                        player2.name = (nameVerified[0])
                        menu = False
                        buttons = False
                        showInputName = False
                        names = 0

    pygame.display.update()
