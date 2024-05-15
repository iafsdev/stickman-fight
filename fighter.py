import pygame

class Fighter():
  def __init__(self, player, x, y, flip, animations) -> None:
    self.player = player 
    self.flip = flip
    self.action = 'idle' # 0: idle, 1: sprint, 2: jump
    self.frame_index = 0
    self.animations = animations
    self.image = self.animations['idle'][0]
    self.update_time = pygame.time.get_ticks()
    self.offset = [280, 200]
    self.scale = 0.25
    self.rect = pygame.Rect((x, y, 40, 90))
    self.vel_y = 0
    self.running = False
    self.jump = False
    self.attacking = False
    self.attack_cooldown =  0
    self.health = 100
    self.alive = True
    
  def move(self, screen_width, screen_height, surface, target, round_over):
    SPEED = 10
    GRAVITY = 2
    dx = 0
    dy = 0
    self.running = False
    
    # Obtener las teclas
    key = pygame.key.get_pressed()
    
    #Solo puede realizar otras acciones si no esta atacando actualmente
    if not self.attacking and self.alive and not round_over:
      # Controles jugador 1
      if self.player == 1:
        # Movimiento
        if key[pygame.K_a]:
          dx = -SPEED
          self.running = True
        if key[pygame.K_d]:
          dx = SPEED
          self.running = True
          
        # Salto
        if key[pygame.K_w] and self.jump == False:
          self.vel_y = -30
          self.jump = True
        
        # Ataques
        if key[pygame.K_c]:
          self.attack(target)
      
      # Controles jugador 2
      if self.player == 2:
        # Movimiento
        if key[pygame.K_j]:
          dx = -SPEED
          self.running = True
        if key[pygame.K_l]:
          dx = SPEED
          self.running = True
          
        # Salto
        if key[pygame.K_i] and self.jump == False:
          self.vel_y = -30
          self.jump = True
        
        # Ataques
        if key[pygame.K_n] or key[pygame.K_m]:
          self.attack(target)

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
      
    # Aplicar un cooldown en el ataque
    if self.attack_cooldown > 0:
      self.attack_cooldown -= 1

    # Actualizar la posición del jugador
    self.rect.x += dx
    self.rect.y += dy
    
  # Actualizar animaciones
  def update(self):
    # Checar la accción que se esta ejecutando
    if self.health <= 0:
      self.health = 0
      self.alive = False
      self.update_action('death')
    elif self.attacking:
      self.update_action('attack')
    elif self.jump:
      self.update_action('jump')
    elif self.running:
      self.update_action('sprint')
    else:
      self.update_action('idle')
    
    animation_cooldown = 23
    self.image = self.animations[self.action][self.frame_index]
    # Aplica un cooldown entre animcaciones
    if pygame.time.get_ticks() - self.update_time > animation_cooldown:
      self.frame_index += 1
      self.update_time = pygame.time.get_ticks()
    # Checa si hay más animación
    if self.frame_index >= len(self.animations[self.action]):
      # Checa si el jugador está muerto
      if not self.alive:
        self.frame_index = len(self.animations[self.action]) - 1
      else:
        self.frame_index = 0
        # Checa si se terminó de atacar
        if self.action == 'attack':
          self.attacking = False
          self.attack_cooldown = 12
      

  def attack (self, target):
    if self.attack_cooldown == 0:
      self.attacking = True
      attacking_rect = pygame.Rect(self.rect.centerx - (0.9 * self.rect.width * self.flip), self.rect.y,  0.9 *self.rect.width, self.rect.height)
      if attacking_rect.colliderect(target.rect):
        target.health -= 5
    
  def update_action(self, new_action):
    # Checa si la nueva acción es diferente a la actual
    if new_action != self.action:
      self.action = new_action
      # Actualizar las configuración de la animación
      self.frame_index = 0
      self.update_time = pygame.time.get_ticks()
      

  def draw(self, surface):
    img = pygame.transform.flip(self.image, self.flip, False)
    # pygame.draw.rect(surface, (255, 0, 0), self.rect)
    surface.blit(img, (self.rect.x - (self.offset[0] * self.scale), self.rect.y - (self.offset[1] * self.scale)))