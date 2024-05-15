import pygame
from fighter import Fighter
from animations import get_animations

pygame.init()

# Crear la ventana
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 640

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
pygame.display.set_caption('Stickman Fight')

# Configurar el framerate
clock = pygame.time.Clock()
FPS = 60

# Definir los colores
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Variable de Juego
intro_count = 3
last_count_update = pygame.time.get_ticks()
show_image = False
show_image_time = 0
round_over = False
ROUND_OVER_COOLDOWN = 2000

# Cargar imágen del fondo
bg_image = pygame.image.load('./assets/images/background/plataforma1.png').convert_alpha()
bg_image_2 = pygame.image.load('./assets/images/background/Fonfoooo.png').convert_alpha()

victory_img = pygame.image.load('./assets/images/background/Letras VictoryFinal.png').convert_alpha()
fight_img = pygame.image.load('./assets/images/background/Letras Fight.png').convert_alpha()

# obtener animaciones
animations = get_animations()

# Función para mostrar el fondo
def draw_bg():
    scaled_bg_2 = pygame.transform.scale(bg_image_2, (SCREEN_WIDTH, SCREEN_HEIGHT))
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg_2, (0,0))
    screen.blit(scaled_bg, (0,0))

# Función para dibujar la barra de vida de los personajes
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))

# Crear dos peleadores
fighter_1 = Fighter(1, 200, 400, False, animations)
fighter_2 = Fighter(2, 700, 400, True, animations)


# Ejecución del juego

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('darkorchid2')
    
    clock.tick(FPS)
    
    # Dibujar el fondo
    draw_bg()
    
    #Mostrar la vida del jugador
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 600, 20)

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

    # Actualizar peleadores
    fighter_1.update()
    fighter_2.update()
    
    # Dibujar los peleadores
    fighter_1.draw(screen)
    fighter_2.draw(screen)
    
    # checa si algun jugador perdió
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
            fighter_1 = Fighter(1, 200, 400, False, animations)
            fighter_2 = Fighter(2, 700, 400, True, animations)
            
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    pygame.display.update()
# Quitar pygame
pygame.quit()