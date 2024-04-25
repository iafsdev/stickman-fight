import pygame

pygame.init()

# Crear la ventana
SCREEN_WIDTH = 1000
SCREEN_HEIGT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGT))
pygame.display.set_caption('Stickman Fight')

# Cargar imágen del fondo
bg_image = pygame.image.load('./assets/images/background/fondo.png').convert_alpha()

# Función para mostrar el fondo
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGT))
    screen.blit(scaled_bg, (0,0))

# Ejecución del juego
run = True
while run:
    # Dibujar el fondo
    draw_bg()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    pygame.display.update()
# Quitar pygame
pygame.quit()