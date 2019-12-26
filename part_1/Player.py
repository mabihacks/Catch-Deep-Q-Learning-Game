class Player:
    def __init__(self, x, y, width, height, speed, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.score = 0
    
    def draw(self, pygame, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
        
    def left(self):
        self.x -= self.speed
        self.x = 0 if self.x < 0 else self.x
        
    def right(self):
        self.x += self.speed
        self.x = (500 - self.width) if self.x + self.width > 500 else self.x
        