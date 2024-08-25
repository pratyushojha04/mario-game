import pygame
from player import Player
from level import Level
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
import asyncio
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Start player in the air
player_start_x = 100
player_start_y = 200  # Start in the air, far from platforms
player = Player(player_start_x, player_start_y)

level = Level('/home/pratyush/Documents/mario game/levels/level1.json')


async def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update player and level
        level.update()
        player.update(level.platforms)

        # Draw everything
        screen.fill((135, 206, 235))  # Sky blue background
        level.draw(screen)
        screen.blit(player.image, player.rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    await asyncio.sleep(0)
asyncio.run(main())
