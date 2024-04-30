import pygame 
class Fighter():
  def __init__(self, x, y) -> None:
    self.rect = pygame.Rect((x, y, 40, 90))
    self.vel_y = 0
    self.jump = False
    self.attack_type =  0
    
  def move(self, screen_width, screen_height, surface, target):
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
    
    # Ataques
    if key[pygame.K_r] or key[pygame.K_t]:
      self.attack(surface, target)
      # Determinar el ataque usado
      if key[pygame.K_r]:
        self.attack_type = 1
      if key[pygame.K_t]:
        self.attack_type = 2


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

  def attack (self, surface, target):
    attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, 2 * self.rect.width, self.rect.height)
    if attacking_rect.collidedict(target.rect):
      print("Hit")
    pygame.draw.rect(surface, (0, 255, 0), self.rect)

  def draw(self, surface):
    pygame.draw.rect(surface, (255, 0, 0), self.rect)