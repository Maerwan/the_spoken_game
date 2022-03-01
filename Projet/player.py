import pygame

# classe joueur
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.velocity = 15
        self.image = pygame.image.load('assets/red_ball.png')
        self.rect = self.image.get_rect()
        self.rect.x = 700
        self.rect.y = 440

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity