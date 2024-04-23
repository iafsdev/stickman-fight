import sys

import pygame

class Game:
    def __init__(self) -> None:
        
        pygame.init()

        pygame.display.set_caption('stickman fight')
        self.screen = pygame.display.set_mode((640, 480))

        self.clock = pygame.time.Clock()
        
        self.img = pygame.image.load('./data/character/mono.png')
        
        self.img_pos = [160, 260]
        self.movement = [False, False]
    def run(self):
        while True:
            self.screen.fill((14, 219, 248))
            self.img_pos[0] += (self.movement[0] - self.movement[1]) * 5
            self.screen.blit(self.img, self.img_pos)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.movement[0] = True
                    if event.key == pygame.K_LEFT:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.movement[0] = False
                    if event.key == pygame.K_LEFT:
                        self.movement[1] = False
                    
            
            pygame.display.update()
            self.clock.tick(60)
            
Game().run()