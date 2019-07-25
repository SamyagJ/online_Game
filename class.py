import pygame

class player_look:
    def __init__(self):
        self.rect=pygame.Rect=(10,10,20,20)
        self.color=pygame.color(0,0,225)

class player:
    def __init__(self):
        self.pygame.name='bolt'
        self.color=pygame.Color(0,0,225)
    def colorChange(self):
        self.pygame.color=(255,0,0)
    def move(self, movement):
        if movement is 1:
            self.player.move_ip(-2,0)
        if movement is 2:
            self.player.move_ip(2,0)
        if movement is 3:
            self.player.move_ip(0,-2)
        if movement is 4:
            self.player.move_ip(2,0)

        def handleCollision():
            if self.box.rect.colliderect(rect):
                self.box.colorChange








