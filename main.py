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


walking_images = []
for i in range(7):
    i += 1
    img = pygame.image.load(
        f"assets\\images\\characters\\player\\walking\\Walking_KG_2_{i}.PNG")
    img = scale_image(img, constants.SCALE_PLAYER)
    walking_images.append(img)

idle_images = []
for i in range(4):
    i += 1
    img = pygame.image.load(
        f"assets\\images\\characters\\player\\iddle\\Idle_KG_1_{i}.PNG")

    img = scale_image(img, constants.SCALE_PLAYER)
    idle_images.append(img)


player = Player(50, 50, walking_images, idle_images)


# variables de movimiento del jugador

move_up = False
move_down = False
move_right = False
move_left = False
walking = False
idle = True

# Controlar el frame rate
clock = pygame.time.Clock()

running = True
while running:

    clock.tick(constants.FPS)

    screen.fill(constants.COLOR_BG)

    # Calcular movimiento del jugador
    delta_x = 0
    delta_y = 0

    if move_up:
        delta_y = -constants.SPEED

    if move_down:
        delta_y = constants.SPEED

    if move_right:
        delta_x = constants.SPEED
        walking = True

    if move_left:
        delta_x = -constants.SPEED
        walking = True

    if not (move_left or move_right):
        walking = False
        idle = True

    if walking:
        player.walking()
        idle = False

    if idle:
        player.idle()
        walking = False
    # Mover jugador
    player.move(delta_x, delta_y)

    player.draw(screen)
    for event in pygame.event.get():
        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                move_left = True
            if event.key == pygame.K_d:
                move_right = True
            if event.key == pygame.K_s:
                move_down = True
            if event.key == pygame.K_w:
                move_up = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_d:
                move_right = False
            if event.key == pygame.K_s:
                move_down = False
            if event.key == pygame.K_w:
                move_up = False

    pygame.display.update()

    # Fill the screen with a color (RGB)
    screen.fill((0, 0, 0))

    # Update the display
    pygame.display.flip()
pygame.quit()
