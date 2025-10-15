import pygame
import constants
from player import Player
from weapon import Weapon

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode(
    (constants.WIDTH, constants.HEIGHT), pygame.SCALED)
pygame.display.set_caption("My First Pygame Game")

# Función para escalar imágenes


def scale_image(image, scale):
    width = image.get_width()
    height = image.get_height()
    return pygame.transform.scale(image, (int(width * scale), int(height * scale)))

# ==============================================================================
# Cargar imágenes


# Arma
gun_image = pygame.image.load("assets/images/weapons/gun.png").convert_alpha()
gun_image = scale_image(gun_image, constants.SCALE_WEAPON)
gun = Weapon(gun_image)

# Player
walking_images = []
for i in range(1, 8):
    img = pygame.image.load(
        f"assets/images/characters/player/walking/Walking_KG_1_{i}.PNG").convert_alpha()
    walking_images.append(scale_image(img, constants.SCALE_PLAYER))

idle_images = []
for i in range(1, 5):
    img = pygame.image.load(
        f"assets/images/characters/player/iddle/Idle_KG_1_{i}.PNG").convert_alpha()
    idle_images.append(scale_image(img, constants.SCALE_PLAYER))

player = Player(50, 50, walking_images, idle_images)

# Control FPS
clock = pygame.time.Clock()
running = True

# ==============================================================================
# Bucle principal
while running:
    clock.tick(constants.FPS)
    screen.fill(constants.COLOR_BG)

    # -------------------------------
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    delta_x = 0
    delta_y = 0

    if keys[pygame.K_a]:
        delta_x = -constants.SPEED
    if keys[pygame.K_d]:
        delta_x = constants.SPEED
    if keys[pygame.K_w]:
        delta_y = -constants.SPEED
    if keys[pygame.K_s]:
        delta_y = constants.SPEED

    # Determinar si está caminando
    walking = delta_x != 0 or delta_y != 0

    # Actualizar jugador
    player.update(walking)
    player.move(delta_x, delta_y)

    # Actualizar arma
    gun.update(player)

    # Dibujar todo
    player.draw(screen)
    gun.draw(screen)

    # Actualizar pantalla
    pygame.display.flip()

pygame.quit()
