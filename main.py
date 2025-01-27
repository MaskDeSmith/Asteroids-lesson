import pygame
from constants import *
from player import *

def main():
    pygame.init()
    frame_rate = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        dt = frame_rate.tick(60) / 1000
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
if __name__ == "__main__":
    main()