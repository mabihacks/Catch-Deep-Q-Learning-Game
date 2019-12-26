import pygame
from Player import Player
from Particle import Particle
from random import randint
import numpy as np

class Game:
    def __init__(self):
        self.SCREEN_WIDTH = 500
        self.SCREEN_HEIGHT = 300
        
        pygame.init()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        
        self.PARTICLE = None #will contain current Particle object
        self.PLAYER = Player((self.SCREEN_WIDTH - 100) / 2, self.SCREEN_HEIGHT - 20, 100, 20, 5, (80, 80, 80))
        
        
    def generate_particle(self):
        r = randint(1, 100)
        if r <= 50:
            self.PARTICLE = Particle(randint(0, self.SCREEN_WIDTH-15), -15, 15, 15, 5, (255, 0, 0), "red")
        else:
            self.PARTICLE = Particle(randint(0, self.SCREEN_WIDTH-15), -15, 15, 15, 5, (0, 80, 0), "green")

    def overlap(self, rect1, rect2):
        return ((rect1.x < rect2.x+rect2.width) and (rect2.x < rect1.x + rect1.width) and (rect1.y<rect2.y+rect2.height) and (rect2.y < rect1.y+rect1.height))
    
    
    def step(self, move):
        # 1 = no move (will see why in second part)
        if move == 0:
            self.PLAYER.left()
        elif move == 2:
            self.PLAYER.right()
        p = self.PARTICLE
        if p is not None:
            p.fall()
            p.draw(pygame, self.screen)
            if self.overlap(self.PLAYER, p):
                if p.name == "red":
                    self.PLAYER.score -= 1
                else:
                    self.PLAYER.score += 1
                self.PARTICLE = None
            if p.y > self.SCREEN_HEIGHT - p.width:
                self.PARTICLE = None
        if self.PARTICLE is None:
            self.generate_particle()
        self.PLAYER.draw(pygame, self.screen)
        
        
def run():
    GAME = Game()    
    while True:
        pygame.event.get()
        GAME.screen.fill((255, 255, 255))
        
        move = 1
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: move=0
        if pressed[pygame.K_RIGHT]: move=2
        GAME.step(move)
        
        text = GAME.font.render(str(GAME.PLAYER.score), True, (0, 0, 0))
        GAME.screen.blit(text, (20, 20))
        
        pygame.display.flip()
        GAME.clock.tick(120)
        
        
        
        
                
        
        
        
        
        
        
        
        
        
        
        