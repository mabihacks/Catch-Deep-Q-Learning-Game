class Particle:
    def __init__(self, x, y, width, height, speed, color, name):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.name = name
        self.color = color
    
    def draw(self, pygame, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
        
    def fall(self):
        self.y += self.speed
        
