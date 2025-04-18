import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main ():
    pygame.init()
    updateable = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    updateables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updateables, drawables)
    Asteroid.containers = (asteroids, updateables, drawables)
    AsteroidField.containers = (updateables)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    screen = pygame.display.set_mode(((SCREEN_WIDTH, SCREEN_HEIGHT)))
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    #player.containers = (updateables, drawables)

    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(0,0,0))
        for updateable in updateables:
            updateable.update(dt)
        #updateables.update(dt)
        #player.draw(screen)
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()
        dt = clock.tick() / 1000

if __name__ == "__main__":
    main()
