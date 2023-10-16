import pygame

class Player:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.x = width * 0.5
        self.y = height * 0.9
        self.valwidth = width / 12
        self.valheight = height / 40
        self.vel = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.vel
        if keys[pygame.K_RIGHT] and self.x < self.width - self.valwidth:
            self.x += self.vel

    def draw(self):
        pygame.draw.rect(self.screen, (255, 0, 0), (self.x, self.y, self.valwidth, self.valheight))