import pygame
from pygame import Color


class Box:

    def __init__(self):
        self.rect = pygame.Rect(10, 20, 20, 20)
        self.color = Color(0, 0, 0)

    def colorChange(self, color):
        self.color = color


class Player:

    def __init__(self):
        self.lives = 5
        self.box = Box()
        self.box.color = Color(102, 0, 255)
        self.counter = 0

    def assign_color(self, color):
        self.box.colorChange(color)

    def move(self, direction):
        if direction == 'N':
            self.box.rect.move_ip(0, -4)
        elif direction == 'NE':
            self.box.rect.move_ip(2, -2)
        elif direction == 'E':
            self.box.rect.move_ip(4, 0)
        elif direction == 'SE':
            self.box.rect.move_ip(2, 2)
        elif direction == 'S':
            self.box.rect.move_ip(0, 4)
        elif direction == 'SW':
            self.box.rect.move_ip(-2, 2)
        elif direction == 'W':
            self.box.rect.move_ip(-4, 0)
        elif direction == 'NW':
            self.box.rect.move_ip(-2, -2)

    def damage(self):
        self.lives=self.lives-1
        self.counter = 10
        return self.lives > 0
            




class Bullet:

    # Fields:
    # - Rect -> Encapsulation of block sprite in-game
    # - Speed -> Speed of movement on move function

    def __init__(self, index, image_filepath="bullet.png", speed=(10, 0), frames=20):
        self.image = pygame.image.load(image_filepath)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.frames = frames
        self.index = index

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

    def handleCollision(self, player, index):
        if self.index != index:
            if self.rect.colliderect(player.box.rect):
                self.hide()
                return player.damage()
        return True


class Trap:

    def __init__(self):
        self.box = Box()

    def handleCollision(self, player):
        if self.box.rect.colliderect(player.box.rect):
            return player.damage()
        return True