import sys,pygame
from pygame.locals import *
from classes import *
import pygame
import random

pygame.init()

font=pygame.font.SysFont('Times New Roman', 30)
from socket import *
import sys
import pygame
from pygame.locals import *
from pygame.display import *
from classes import Box, Trap, Player


def get_info():
    ret = ""
    while len(ret) == 0 or ret[-1] != '}':
        pkt = s.recv(1024).decode("ascii")
        ret += pkt
    return ret[:-1]


def quit():
    s.close()
    pygame.quit()


def update():
    pygame.event.pump()
    key = pygame.key.get_pressed()
    direction = '{'
    if key[pygame.K_w]:
        direction += 'N'
    elif key[pygame.K_s]:
        direction += 'S'
    if key[pygame.K_d]:
        direction += 'E'
    elif key[pygame.K_a]:
        direction += 'W'
    if key[pygame.K_LEFT]:
        direction += ',W'
    elif key[pygame.K_RIGHT]:
        direction += ',E'
    elif key[pygame.K_UP]:
        direction += ',N'
    elif key[pygame.K_DOWN]:
        direction += ',S'
    else:
        direction += ',Q'
    if key[pygame.K_ESCAPE]:
        quit()
    direction += '}'
    s.send(direction.encode("ascii"))
    print(direction)


def render():
    receival = get_info()
    if len(receival) > 0:
        screen.fill(color=pygame.Color("white"))
        objects = receival.split("=")
        players = objects[0].split('|')[:-1]
        traps = objects[1].split('|')[:-1]
        bullets = objects[2].split('|')[:-1]
        tokens = []
        rect = pygame.Rect(0, 0, 20, 20)
        for i in players:
            tokens = i.split(",")
            rect.center = (int(tokens[0]), int(tokens[1]))
            screen.fill(pygame.Color(int(tokens[2]), int(tokens[3]), int(tokens[4])), rect)
        for i in traps:
            tokens = i.split(",")
            rect.center = (int(tokens[0]), int(tokens[1]))
            screen.fill(pygame.Color(int(tokens[2]), int(tokens[3]), int(tokens[4])), rect)
        rect.width = 5
        rect.height = 5
        for i in bullets:
            tokens = i.split(",")
            rect.center = (int(tokens[0]), int(tokens[1]))
            screen.fill(pygame.Color(67,180,40), rect)


def main():
    while True:
        clock.tick(60)
        render()
        update()
        pygame.display.flip()


## Socket globals
s = socket(AF_INET, SOCK_STREAM)
s.settimeout(10)
s.connect((input("IP Address?\n"), int(input("PORT?\n"))))
s.settimeout(None)
#######

## Pygame Globals
pygame.init()
clock = pygame.time.Clock()
# info = pygame.display.Info()
# (x, y) = (info.current_w, info.current_h)
x, y = 1024, 768
# screen = pygame.display.set_mode((x//2, y//2))
screen = pygame.display.set_mode((x, y))
# x, y = x//2, y//2
###########

if __name__ == "__main__":
    main()
