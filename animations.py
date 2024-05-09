import pygame

def get_animations():
  animations = {}
  size = 720
  scale = 0.25
  # quieto
  img = pygame.image.load('./assets/images/animations/idle/idle.png').convert_alpha()
  idle_list = [pygame.transform.scale(img, (size * scale, size * scale))]
  animations['idle'] = idle_list
  
  # saltar
  jump_list = [pygame.image.load('./assets/images/animations/jump/jump.png').convert_alpha()]
  animations['jump'] = jump_list
  
  return animations