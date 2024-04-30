import pygame
from fighter import Fighter

pygame.init()

# Crear la ventana
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 640

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Stickman Fight')

# Configurar el framerate
clock = pygame.time.Clock()
FPS = 60

# Cargar imágen del fondo
bg_image = pygame.image.load('./assets/images/background/plataforma1.png').convert_alpha()
bg_image_2 = pygame.image.load('./assets/images/background/Fonfoooo.png').convert_alpha()

# Función para mostrar el fondo
def draw_bg():
    scaled_bg_2 = pygame.transform.scale(bg_image_2, (SCREEN_WIDTH, SCREEN_HEIGHT))
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg_2, (0,0))
    screen.blit(scaled_bg, (0,0))

# Crear dos peleadores
fighter_1 = Fighter(200, 400)
fighter_2 = Fighter(700, 400)

# Ejecución del juego
run = True
while run:
    screen.fill('darkorchid2')
    
    clock.tick(FPS)
    
    # Dibujar el fondo
    draw_bg()
    
    # Mover a los peleadores
    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT)
    # fighter_2.move()
    
    # Dibujar los peleadores
    fighter_1.draw(screen)
    fighter_2.draw(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    pygame.display.update()
# Quitar pygame
pygame.quit()