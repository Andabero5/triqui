import pygame
import sys
from board import Board

SIZE = (900, 900)
WHITE = (255, 255, 255)
LINEWDTH = 15
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Triqui")

board = Board()


def lines():
    # vertical lines
    pygame.draw.line(screen, WHITE, (300, 0), (300, 900), LINEWDTH)
    pygame.draw.line(screen, WHITE, (600, 0), (600, 900), LINEWDTH)
    # Horizontal lines
    pygame.draw.line(screen, WHITE, (0, 300), (900, 300), LINEWDTH)
    pygame.draw.line(screen, WHITE, (0, 600), (900, 600), LINEWDTH)


print(board.squares(0, 0, 1))
print(board.isValidSquare(0, 0))


# principal loop
playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
