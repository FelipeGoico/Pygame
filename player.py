import pygame
import constants


class Player():
    def __init__(self, x, y, animation_frames):
        self.flip = False
        self.animation_frames = animation_frames
        self.image = animation_frames[0]
        # imagen de la animacion que se esta mostrando actualmente
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        # self.image = animation_frames[self.frame_index]

        self.shape = pygame.Rect(
            0, 0, constants.WIDTH_PLAYER, constants.HEIGHT_PLAYER)
        self.shape.center = (x, y)

    def update(self):
        # actualizar la animacion del jugador
        animation_cooldown = 100
        # tiempo entre frames de la animacion

        # actualizar la imagen del jugador
        self.image = self.animation_frames[self.frame_index]

        # comprobar si es hora de actualizar la animacion
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            # si la animacion se ha completado, reiniciar
            if self.frame_index >= len(self.animation_frames):
                self.frame_index = 0

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
