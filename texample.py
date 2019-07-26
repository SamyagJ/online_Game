# Tristan Hilbert
# Examples of using bullet class

import pygame, sys
from tclasses import Bullet

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
counter = 0

def spawn_bullet(bullets, dir):
    global counter
    counter += 1
    if counter >= 10:
        if dir is 1:
            bullets.append(Bullet(speed=(0, -10)))
            bullets[-1].rect.center = (320, 240)
            bullets[-1].rotate()
        elif dir is 2:
            bullets.append(Bullet(speed=(10,0)))
            bullets[-1].rect.center = (320, 240)
        elif dir is 3:
            bullets.append(Bullet(speed=(0, -10)))
            bullets[-1].rect.center = (320, 240)
            bullets[-1].flip()
            bullets[-1].rotate()
        else:
            bullets.append(Bullet(speed=(10, 0)))
            bullets[-1].rect.center = (320, 240)
            bullets[-1].flip()
        counter = 0

# lists -> Pass by Reference
def update(bullets):
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        spawn_bullet(bullets, 4)
    elif keys[pygame.K_RIGHT]:
        spawn_bullet(bullets, 2)
    elif keys[pygame.K_UP]:
        spawn_bullet(bullets, 1)
    elif keys[pygame.K_DOWN]:
        spawn_bullet(bullets, 3)
    elif keys[pygame.K_ESCAPE]:
        pygame.quit()

    for i in bullets:
        if i.update(True) == False:
            bullets.remove(i)
    
def render(bullets):
    screen.fill(pygame.Color("black"))
    for i in bullets:
        i.render(screen)

def main():
    bullets = []
    while True:
        clock.tick(60)
        update(bullets)
        render(bullets)
        pygame.display.flip()

if __name__ == "__main__":
    main()

