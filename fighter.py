import pygame 

class Fighter():
  def __init__(self, x, y) -> None:
    self.rect = pygame.Rect((x, y, 40, 90))
    self.vel_y = 0
    self.jump = False
    
  def move(self, screen_width, screen_height):
    SPEED = 10
    GRAVITY = 2
    dx = 0
    dy = 0
    
    # Obtener las teclas
    key = pygame.key.get_pressed()
    
    # Movimiento
    if key[pygame.K_a]:
      dx = -SPEED
    if key[pygame.K_d]:
      dx = SPEED
      
    # Salto
    if key[pygame.K_w] and not self.jump:
      self.vel_y = -30
      self.jump = True
      
    # Aplicar gravedad
    self.vel_y += GRAVITY 
    dy += self.vel_y
      
    # Jugador no salga de la pantalla
    if self.rect.left + dx < 0:
      dx = -self.rect.left
    if self.rect.right + dx > screen_width:
      dx = screen_width - self.rect.right
    if self.rect.bottom + dy > screen_height - 150:
      self.vel_y = 0
      self.jump = False
      dy = screen_height - 150 - self.rect.bottom
      
    # Actualizar la posición del jugador
    self.rect.x += dx
    self.rect.y += dy
      
    
  def draw(self, surface):
    pygame.draw.rect(surface, (255, 0, 0), self.rect)