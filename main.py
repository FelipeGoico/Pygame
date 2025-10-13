import pygame
import constants
from player import Player
# Initialize Pygame
pygame.init()
# Create a window
screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))

pygame.display.set_caption("My First Pygame Game")


def scale_image(image, scale):
    width = image.get_width()
    height = image.get_height()
    new_image = pygame.transform.scale(
        image, (int(width * scale), int(height * scale)))
    return new_image


animation_frames = []
for i in range(7):
    i += 1
    img = pygame.image.load(
        f"assets\\images\\characters\\player\\walking\\Walking_KG_2_{i}.PNG")
    img = scale_image(img, constants.SCALE_PLAYER)
    animation_frames.append(img)


player = Player(50, 50, animation_frames)


# variables de movimiento del jugador

mover_arriba = False
mover_abajo = False
mover_derecha = False
mover_izquierda = False

# Controlar el frame rate
clock = pygame.time.Clock()

running = True
while running:

    clock.tick(constants.FPS)

    screen.fill(constants.COLOR_BG)

    # Calcular movimiento del jugador
    delta_x = 0
    delta_y = 0

    if mover_arriba:
        delta_y = -constants.SPEED
    if mover_abajo:
        delta_y = constants.SPEED
    if mover_derecha:
        delta_x = constants.SPEED
        player.update()
    if mover_izquierda:
        delta_x = -constants.SPEED
        player.update()

    # Mover jugador
    player.move(delta_x, delta_y)

    player.draw(screen)
    for event in pygame.event.get():
        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_s:
                mover_abajo = True
            if event.key == pygame.K_w:
                mover_arriba = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_s:
                mover_abajo = False
            if event.key == pygame.K_w:
                mover_arriba = False

    pygame.display.update()

    # Fill the screen with a color (RGB)
    screen.fill((0, 0, 0))

    # Update the display
    pygame.display.flip()
pygame.quit()
