import pygame
import constants
import math


class Weapon():
    def __init__(self, image):
        self.flip = False
        self.image_original = image
        self.angle = 0
        self.image = pygame.transform.rotate(self.image_original, self.angle)
        self.shape = self.image.get_rect()

    def update(self, player):
        self.shape.center = player.shape.center
        if player.flip == True:
            self.shape.x = self.shape.x - player.shape.width // 2
            self.rotate_gun(True)

        if player.flip == False:
            self.shape.x = self.shape.x + player.shape.width // 2
            self.rotate_gun(False)

        # Mover la pistola con el mouse
        # mouse_pos = pygame.mouse.get_pos()
        # distance_x = mouse_pos[0] - self.shape.centerx
        # distance_y = mouse_pos[1] - self.shape.centery

        # atan2 devuelve el angulo en radianes
        # self.angle = math.degrees(math.atan2(-distance_y, distance_x))

    def rotate_gun(self, rotate):
        if rotate == True:
            image_flip = pygame.transform.flip(self.image, True, False)
            self.image = pygame.transform.rotate(image_flip, self.angle)
        else:
            image_flip = pygame.transform.flip(self.image, False, False)
            self.image = pygame.transform.rotate(image_flip, self.angle)

    def draw(self, screen):
        screen.blit(self.image, self.shape)
        # pygame.draw.rect(screen, constants.COLOR_GUN, self.shape, 1)
