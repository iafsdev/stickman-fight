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
  img = pygame.image.load('./assets/images/animations/jump/jump.png').convert_alpha()
  jump_list = [pygame.transform.scale(img, (size * scale, size * scale))]
  animations['jump'] = jump_list
  
  # correr
  sprint_list = []
  for i in range(1,53):
    img = pygame.image.load(f'./assets/images/animations/sprint/{i}.png').convert_alpha()
    sprint_list.append(pygame.transform.scale(img, (size * scale, size * scale)))
  animations['sprint'] = sprint_list
  
  # atacar
  attack_list = []
  for i in range(1,15):
    img = pygame.image.load(f'./assets/images/animations/attack/{i}.png').convert_alpha()
    attack_list.append(pygame.transform.scale(img, (size * scale, size * scale)))
  animations['attack'] = attack_list
  
  death_list = []
  for i in range(1,60):
    img = pygame.image.load(f'./assets/images/animations/death/{i}.png').convert_alpha()
    death_list.append(pygame.transform.scale(img, (size * scale, size * scale)))
  animations['death'] = death_list
  
  return animations