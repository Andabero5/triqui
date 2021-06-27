import pygame
import constants

pygame.init()


class Button:
    def __init__(self, text,  pos, font, bg):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Corbel", font)
        self.text = self.font.render(text, 1, pygame.Color("black"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(pygame.Color(bg))
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self, screen):
        screen.blit(self.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    return True


class Input:
    def __init__(self):
        self.name = ''
        self.rect = pygame.Rect(200, 425, 500, 50)
        self.font = pygame.font.SysFont("Corbel", 50)

    def show(self, screen, nPlayer):
        inputRect = pygame.draw.rect(screen, constants.WHITE, self.rect, 2)
        textSurface = self.font.render(self.name, True, constants.WHITE)
        screen.blit(textSurface, (self.rect.x + 5, self.rect.y + 5))
        textSurface = self.font.render(
            f"Ingrese el nombre del jugador {nPlayer}", True, constants.WHITE)
        screen.blit(textSurface, (self.rect.x-60, self.rect.y - 100))
        inputRect.w = max(100, textSurface.get_width())

    def keys(self, event, screen):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.name = self.name[:-1]
                screen.fill(pygame.Color('black'))
            elif len(self.name) < 15:
                self.name += event.unicode
            if event.key == pygame.K_RETURN:
                return [self.name, True]
        return ["", False]
