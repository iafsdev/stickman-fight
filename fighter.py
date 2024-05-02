import pygame

class Fighter():
  def __init__(self, player, x, y) -> None:
    self.player = player 
    self.flip = False
    self.rect = pygame.Rect((x, y, 40, 90))
    self.vel_y = 0
    self.jump = False
    self.attacking = False
    self.attack_type =  0
    self.health = 100
    
  def move(self, screen_width, screen_height, surface, target):
    SPEED = 10
    GRAVITY = 2
    dx = 0
    dy = 0
    
    # Obtener las teclas
    key = pygame.key.get_pressed()
    
    #Solo puede realizar otras acciones si no esta atacando actualmente
    if self.attacking == False:
      # Controles jugador 1
      if self.player == 1:
        # Movimiento
        if key[pygame.K_a]:
          dx = -SPEED
        if key[pygame.K_d]:
          dx = SPEED
          
        # Salto
        if key[pygame.K_w] and self.jump == False:
          self.vel_y = -30
          self.jump = True
        
        # Ataques
        if key[pygame.K_c] or key[pygame.K_v]:
          self.attack(surface, target)
          # Determinar el ataque usado
          if key[pygame.K_c]:
            self.attack_type = 1
          if key[pygame.K_v]:
            self.attack_type = 2
          self.attacking = False
      
      # Controles jugador 2
      if self.player == 2:
        # Movimiento
        if key[pygame.K_j]:
          dx = -SPEED
        if key[pygame.K_l]:
          dx = SPEED
          
        # Salto
        if key[pygame.K_i] and self.jump == False:
          self.vel_y = -30
          self.jump = True
        
        # Ataques
        if key[pygame.K_n] or key[pygame.K_m]:
          self.attack(surface, target)
          # Determinar el ataque usado
          if key[pygame.K_n]:
            self.attack_type = 1
          if key[pygame.K_m]:
            self.attack_type = 2
          self.attacking = False

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

    # Poner en cara cada jugador
    if target.rect.centerx > self.rect.centerx:
      self.flip = False
    else:
      self.flip = True

    # Actualizar la posición del jugador
    self.rect.x += dx
    self.rect.y += dy

  def attack (self, surface, target):
    self.attacking = True
    attacking_rect = pygame.Rect(self.rect.centerx - (2 * self. rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
    if attacking_rect.colliderect(target.rect):
      target.health -= 10
    pygame.draw.rect(surface, (0, 255, 0), self.rect)

  def draw(self, surface):
    pygame.draw.rect(surface, (255, 0, 0), self.rect)