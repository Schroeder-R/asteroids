import pygame
from constants import *
from player import Player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # pygame initialization
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # game variables
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        

        screen.fill((0, 0, 0))  # clear the screen

        # player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
        player.update(dt)
        player.draw(screen)

        pygame.display.flip()

        # frame_count += 1
        # if time.time() - start_time > 1:
        #     print(f"FPS: {frame_count}")
        #     frame_count = 0
        #     start_time = time.time()

        dt = clock.tick(144) / 1000.0  # limit the FPS to 60 and convert to seconds

if __name__ == "__main__":
    main()