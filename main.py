import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():

    # pygame initialization
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable,)
    Shot.containers = (shots, updateable, drawable)

    # game variables
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updateable:
            obj.update(dt)
        
        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                print("Game Over!")
                sys.exit()

            for shot in shots:
                if shot.is_colliding(asteroid):
                    asteroid.split()
            
        screen.fill((0, 0, 0))  # clear the screen

        for obj in drawable:
            obj.draw(screen)  # draw the game objects to the screen

        pygame.display.flip()

        dt = clock.tick(144) / 1000.0  # limit the FPS to 60 and convert to seconds

if __name__ == "__main__":
    main()