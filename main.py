import pygame
from constants import *
from player import Player

def main():

    # pygame initialization
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    # game variables
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        screen.fill((0, 0, 0))  # clear the screen

        for obj in drawable:
            obj.draw(screen)  # draw the game objects to the screen

        pygame.display.flip()

        dt = clock.tick(144) / 1000.0  # limit the FPS to 60 and convert to seconds

if __name__ == "__main__":
    main()