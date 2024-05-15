import pygame
import sys
from fighter import Fighter
from animations import get_animations

def main_loop():
    pygame.init()

    # Define todas las variables globales necesarias, como SCREEN_WIDTH, SCREEN_HEIGHT, etc.
    SCREEN_WIDTH = 1024
    SCREEN_HEIGHT = 640
    FPS = 60

    # Crear la ventana
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Stickman Fight')

    # Configurar el framerate
    clock = pygame.time.Clock()

    # Define los colores
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)

    # Variable de Juego
    intro_count = 3
    last_count_update = pygame.time.get_ticks()
    score = [0, 0]
    show_image = False
    show_image_time = 0
    round_over = False
    ROUND_OVER_COOLDOWN = 2000

    # Cargar imágenes
    bg_image = pygame.image.load('./assets/images/background/plataforma1.png').convert_alpha()
    bg_image_2 = pygame.image.load('./assets/images/background/Fonfoooo.png').convert_alpha()
    victory_img = pygame.image.load('./assets/images/background/Letras VictoryFinal.png').convert_alpha()
    fight_img = pygame.image.load('./assets/images/background/Letras Fight.png').convert_alpha()
    score_font = pygame.font.Font('./assets/fonts/turok.ttf', 30)

    # Función para dibujar Texto
    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    # Función para mostrar el fondo
    def draw_bg():
        scaled_bg_2 = pygame.transform.scale(bg_image_2, (SCREEN_WIDTH, SCREEN_HEIGHT))
        scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(scaled_bg_2, (0, 0))
        screen.blit(scaled_bg, (0, 0))

    # Función para dibujar la barra de vida de los personajes
    def draw_health_bar(health, x, y):
        ratio = health / 100
        pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
        pygame.draw.rect(screen, RED, (x, y, 400, 30))
        pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))

    # Crear dos peleadores
    fighter_1 = Fighter(1, 200, 400, False, get_animations())
    fighter_2 = Fighter(2, 700, 400, True, get_animations())

    # Ejecución del juego
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

        screen.fill('darkorchid2')
        clock.tick(FPS)

        # Dibujar el fondo
        draw_bg()

        # Mostrar la vida del jugador
        draw_health_bar(fighter_1.health, 20, 20)
        draw_health_bar(fighter_2.health, 600, 20)
        draw_text("P1: " + str(score[0]), score_font, RED, 20, 60)
        draw_text("P2: " + str(score[0]), score_font, RED, 598, 60)

        # Actualizar contador
        time_now = pygame.time.get_ticks()
        time_elapsed = (time_now - last_count_update) / 1000  # Convertir a segundos

        if intro_count > 0:
            # Actualizar el contador
            if time_elapsed >= 1:
                intro_count -= 1
                last_count_update = time_now
                print(intro_count)
        else:
            # Mostrar la imagen durante 2 segundos al llegar a cero el contador
            if not show_image:
                show_image = True
                show_image_time = time_now

            if show_image and time_now - show_image_time < 1000:
                screen.blit(fight_img, (0, 20))
            else:
                # Mostrar la imagen de fondo y mover a los peleadores
                fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)
                fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1)

        # Dibujar los peleadores
        fighter_1.draw(screen)
        fighter_2.draw(screen)

        # Checar si algún jugador perdió
        if not round_over:
            if not fighter_1.alive:
                round_over = True
                round_over_time = pygame.time.get_ticks()
            elif not fighter_2.alive:
                round_over = True
                round_over_time = pygame.time.get_ticks()
        else:
            screen.blit(victory_img, (0, 20))
            if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
                round_over = False
                intro_count = 3
                show_image = False  # Reinicia la variable show_image
                fighter_1 = Fighter(1, 200, 400, False, get_animations())
                fighter_2 = Fighter(2, 700, 400, True, get_animations())

        pygame.display.update()

    pygame.quit()

# Llama a la función del bucle principal para iniciar el juego
main_loop()
