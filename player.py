import pygame
import constants


class Player():
    def __init__(self, x, y, walking_images, idle_images):
        self.flip = False
        self.walking_images = walking_images
        self.idle_images = idle_images
        self.image = idle_images[0]
        # imagen de la animacion que se esta mostrando actualmente
        self.walking_index = 0
        self.idle_index = 0
        self.update_time = pygame.time.get_ticks()
        # self.image = walking_images[self.walking_index]

        self.shape = self.image.get_rect()
        self.shape.center = (x, y)

    def walking(self):
        # actualizar la animacion del jugador
        animation_cooldown = 100
        # tiempo entre frames de la animacion

        # actualizar la imagen del jugador
        self.image = self.walking_images[self.walking_index]

        # comprobar si es hora de actualizar la animacion
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.walking_index += 1
            # si la animacion se ha completado, reiniciar
            if self.walking_index >= len(self.walking_images):
                self.walking_index = 0

    def idle(self):
        # actualizar la animacion del jugador
        animation_cooldown = 100
        # tiempo entre frames de la animacion

        # actualizar la imagen del jugador
        self.image = self.idle_images[self.idle_index]

        # comprobar si es hora de actualizar la animacion
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.idle_index += 1
            # si la animacion se ha completado, reiniciar
            if self.idle_index >= len(self.idle_images):
                self.idle_index = 0

    def draw(self, screen):
        image_flip = pygame.transform.flip(self.image, self.flip, False)
        screen.blit(image_flip, self.shape)
        # pygame.draw.rect(screen, constants.COLOR_PLAYER, self.shape, 1)

    def move(self, delta_x, delta_y):
        if delta_x < 0:
            self.flip = True
        elif delta_x > 0:
            self.flip = False
        self.shape.x = self.shape.x + delta_x
        self.shape.y = self.shape.y + delta_y
