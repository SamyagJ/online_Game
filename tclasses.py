# Tristan Hilbert
#   7/25/2019
# This encapsulates the necessary classes for cloned temporary
# objects.

import pygame

class Bullet:

    # Fields:
    # - Rect -> Encapsulation of block sprite in-game
    # - Speed -> Speed of movement on move function

    def __init__(self, image_filepath="bullet.png", speed=(10, 0), frames=20):
        self.image = pygame.image.load(image_filepath)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.frames = frames
    
    def flip(self):
        self.image = pygame.transform.flip(self.image, True, False)
        self.speed = (self.speed[0] * -1, self.speed[1] * -1)
    
    def rotate(self, neg=False):
        if neg:
            self.image = pygame.transform.rotate(self.image, 270)
        else:
            self.image = pygame.transform.rotate(self.image, 90)

    def move(self):
        self.rect.move_ip(self.speed)
    
    def update(self, move_bool=False):
        if move_bool:
            self.move()
        self.frames -= 1
        return self.frames >= 0

    def render(self, surface):
        surface.blit(self.image, self.rect)
    
    def collides(self, rect):
        return self.rect.colliderect(rect)

    def hide(self):
        self.frames = -1
    
    