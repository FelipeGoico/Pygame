import pygame
import constants
import math


class Weapon:
    def __init__(self, image):
        self.image_original = image
        self.image = image
        self.shape = self.image.get_rect()
        self.angle = 0
        # Offset opcional para que el arma quede pegada al brazo
        self.offset_x = 15
        self.offset_y = 5

    def update(self, player):
        # Posición base del arma según jugador y dirección
        if player.flip:
            # Flip horizontal si el jugador mira a la izquierda
            self.image = pygame.transform.flip(
                self.image_original, True, False)
            base_x = player.shape.centerx - self.offset_x
        else:
            self.image = self.image_original
            base_x = player.shape.centerx + self.offset_x

        base_y = player.shape.centery + self.offset_y
        self.shape.center = (base_x, base_y)

        # -----------------------------
        # Calcular ángulo hacia el mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx = mouse_x - self.shape.centerx
        dy = mouse_y - self.shape.centery

        # atan2 devuelve el ángulo en radianes
        self.angle = math.degrees(math.atan2(-dy, dx))

        # Rotar la imagen
        self.image = pygame.transform.rotate(self.image, self.angle)
        # Actualizar rect según rotación
        self.shape = self.image.get_rect(center=self.shape.center)

    def draw(self, screen):
        screen.blit(self.image, self.shape)
        # pygame.draw.rect(screen, constants.COLOR_GUN, self.shape, 1)
