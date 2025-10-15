import pygame
import constants


class Weapon:
    def __init__(self, image):
        self.image_original = image
        self.image = image
        self.shape = self.image.get_rect()
        self.angle = 0

    def update(self, player):
        # Centrar el arma respecto al jugador
        self.shape.center = player.shape.center

        if player.flip:
            # Si el jugador mira a la izquierda
            self.image = pygame.transform.flip(
                self.image_original, True, False)
            self.shape.x -= player.shape.width // 2
        else:
            # Si mira a la derecha
            self.image = self.image_original
            self.shape.x += player.shape.width // 2

    def draw(self, screen):
        screen.blit(self.image, self.shape)
        pygame.draw.rect(screen, constants.COLOR_GUN, self.shape, 1)
