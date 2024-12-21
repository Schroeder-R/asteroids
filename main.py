import pygame
from constants import *
import time

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # pygame initialization
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    frame_count = 0
    start_time = time.time()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))  # clear the screen
        pygame.display.flip()

        frame_count += 1
        if time.time() - start_time > 1:
            print(f"FPS: {frame_count}")
            frame_count = 0
            start_time = time.time()

        dt = clock.tick(144) / 1000.0  # limit the FPS to 60 and convert to seconds

if __name__ == "__main__":
    main()