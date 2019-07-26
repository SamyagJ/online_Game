from classes import Box, Trap, Player, Bullet
from pygame import Color
import random
import sys
import socket
import time
import traceback
import pygame


ipv4_address = '127.0.0.1'
port = 7027

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ipv4_address, port))
###################

# Server Game Info

map_width = 1024
map_height = 768
traps = []
players = []


#############

# Auxillary Class


class ServerPlayer(Player):

    def __init__(self, connection):
        Player.__init__(self)
        self.connection = connection


def spawn():
    x = 0
    y = 0
    for i in range(30):
        traps.append(Trap())
        x = random.randint(0, map_width - 20)
        y = random.randint(0, map_width - 20)
        traps[-1].box.rect.center = (x, y)
    for i in players:
        x = random.randint(0, map_width - 20)
        y = random.randint(0, map_width - 20)
        i.box.rect.center = (x, y)
        i.box.color = Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

counter = 0

def spawn_bullet(bullets, dir, pos, pli):
    global counter
    counter += 1
    if counter >= 10:
        if dir is 'N':
            bullets.append(Bullet(pli, speed=(0, -10)))
            bullets[-1].rect.center = (pos[0], pos[1])
            bullets[-1].rotate()
        elif dir is 'E':
            bullets.append(Bullet(pli, speed=(10,0)))
            bullets[-1].rect.center = (pos[0], pos[1])
        elif dir is 'S':
            bullets.append(Bullet(pli, speed=(0, -10)))
            bullets[-1].rect.center = (pos[0], pos[1])
            bullets[-1].flip()
            bullets[-1].rotate()
        else:
            bullets.append(Bullet(pli, speed=(10, 0)))
            bullets[-1].rect.center = (pos[0], pos[1])
            bullets[-1].flip()
        counter = 0


def update(bullets):
    for i in players:
        command = i.connection.recv(1024).decode("ascii")
        if len(command) > 0:
            command = command[1:-1]

        if len(command) > 0:
            direction = command[:command.index(',')]
            shoot = command[command.index(',') + 1:]
            if len(direction) > 1 and direction[0] != 'N' and direction[0] != 'S':
                direction = direction[:-1]
            if len(direction) > 1 and direction[1] != 'E' and direction[1] != 'W':
                direction = direction[:-1]
            i.move(direction)
            if shoot != 'Q':
                spawn_bullet(bullets, shoot, i.box.rect.center, players.index(i))

        for j in traps:
            j.handleCollision(i)

        for j in bullets:
            j.handleCollision(i, players.index(i))


def send(bullets):
    manip = ''
    for j in players:
        manip = ''
        manip += str(j.box.rect.centerx) + ',' + str(j.box.rect.centery)
        manip += ',' + str(j.box.color.r) + ',' + str(j.box.color.g)
        manip += ',' + str(j.box.color.b)
        manip += '|'
    manip += '='
    for j in traps:
        manip += str(j.box.rect.centerx) + ',' + str(j.box.rect.centery)
        manip += ',' + str(j.box.color.r) + ',' + str(j.box.color.g)
        manip += ',' + str(j.box.color.b)
        manip += '|'
    manip += '='
    for j in bullets:
        if j.update():
            manip += str(j.rect.centerx) + ',' + str(j.rect.centery)
            manip += '|'
        else:
            bullets.remove(j)
    manip += '}'
    for i in players:
        i.connection.send(manip.encode("ascii"))


def main():
    while True:
        try:
            a = 0
            while a != 1:
                try:
                    sock.settimeout(20)
                    sock.listen(0)
                    print("Started Connection!")

                    conn, addr = sock.accept()
                    conn.settimeout(None)
                    players.append(ServerPlayer(conn))
                    print("Connection!")
                except socket.timeout:
                    print("Timeout!")
                finally:
                    a = int(input("Continue Checking?"))
                    if a == 2:
                        raise Exception("Clear Game!")
            sock.settimeout(None)
            spawn()
            bullets = []
            while len(players) > 0:
                send(bullets)
                update(bullets)

        except Exception:
            traceback.print_exc()

        finally:
            for i in players:
                i.connection.close()
            sock.close()
            break


if __name__ == "__main__":
    main()
