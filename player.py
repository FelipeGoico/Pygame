import pygame
import constants


class Player:
    def __init__(self, x, y, walking_images, idle_images):
        self.flip = False
        self.walking_images = walking_images
        self.idle_images = idle_images
        self.image = idle_images[0]

        # Índices y tiempos de animación
        self.walking_index = 0
        self.idle_index = 0
        self.animation_cooldown = 100  # ms entre frames
        self.last_update = pygame.time.get_ticks()

        # Rectángulo de colisión / posición
        self.shape = self.image.get_rect(center=(x, y))

        # Estado
        self.state = "idle"  # "walking" o "idle"

    def update(self, moving):
        """Actualiza animación según el estado actual."""
        current_time = pygame.time.get_ticks()
        if moving:
            self.state = "walking"
        else:
            self.state = "idle"

        # Controlar el frame según el estado
        if current_time - self.last_update >= self.animation_cooldown:
            self.last_update = current_time

            if self.state == "walking":
                self.walking_index = (
                    self.walking_index + 1) % len(self.walking_images)
            else:
                self.idle_index = (self.idle_index + 1) % len(self.idle_images)

        # Actualizar imagen actual
        if self.state == "walking":
            self.image = self.walking_images[self.walking_index]
        else:
            self.image = self.idle_images[self.idle_index]

    def move(self, delta_x, delta_y):
        """Mueve al jugador y ajusta flip."""
        if delta_x < 0:
            self.flip = True
        elif delta_x > 0:
            self.flip = False

        self.shape.x += delta_x
        self.shape.y += delta_y

    def draw(self, screen):
        """Dibuja al jugador en pantalla."""
        image_to_draw = pygame.transform.flip(self.image, self.flip, False)
        screen.blit(image_to_draw, self.shape)
        # pygame.draw.rect(screen, constants.COLOR_PLAYER, self.shape, 1)
