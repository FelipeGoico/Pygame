import pygame
import constants


class Player():
    def __init__(self, x, y, image):
        self.image = image
        self.shape = pygame.Rect(
            0, 0, constants.WIDTH_PLAYER, constants.HEIGHT_PLAYER)
        self.shape.center = (x, y)

    def draw(self, screen):
        screen.blit(self.image, self.shape)
        # pygame.draw.rect(screen, constants.COLOR_PLAYER, self.shape, 1)

    def move(self, delta_x, delta_y):
        self.shape.x = self.shape.x + delta_x
        self.shape.y = self.shape.y + delta_y
