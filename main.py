# Importa la librería
import pygame

# Inicia el juego y crea las variables necesarias
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# Calcula la posición donde va iniciar el jugador, en este caso el centro de la pantalla
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("darkorchid3")

    # pygame.draw.circle(screen, "red", player_pos, 40)

    # # Comprueba que tecla está siendo presionada
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_UP]:
    #     player_pos.y -= 200 * dt
    # if keys[pygame.K_DOWN]:
    #     player_pos.y += 200 * dt
    # if keys[pygame.K_LEFT]:
    #     player_pos.x -= 200 * dt
    # if keys[pygame.K_RIGHT]:
    #     player_pos.x += 200 * dt

    # Actualiza la pantalla
    pygame.display.flip()

    # Determina cuanto es el tiempo para cada frame para actualizar el desplazamiento y ajusta un límite de FPS

pygame.quit()