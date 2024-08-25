import os
import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        base_path = os.path.dirname(os.path.dirname(__file__))
        self.image = pygame.image.load(os.path.join(base_path, 'assets/images/mario.png'))
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocity_y = 0
        self.on_ground = False
        self.game_started = False
        self.score = 0  # Initialize the score

    def update(self, platforms):
        keys = pygame.key.get_pressed()

        # Control Mario's vertical movement
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

        # Implement gravity, but only if the player is not moving up
        if not keys[pygame.K_UP]:
            self.velocity_y += 0.5
        else:
            self.velocity_y = 0

        self.rect.y += 0.02*self.velocity_y

        # Check for collision with platforms
        collided_platform = pygame.sprite.spritecollideany(self, platforms)
        if collided_platform:
            if self.rect.bottom >= collided_platform.rect.top:
                self.rect.bottom = collided_platform.rect.top
                self.velocity_y = 0
                self.on_ground = True
                self.game_started = True
        else:
            self.on_ground = False

        # Increase score while the game is ongoing
        if self.game_started:
            self.score += 1

        # Game over if Mario falls off the screen or is not on a platform after game start
        if self.game_started and (self.rect.top > SCREEN_HEIGHT or not self.on_ground):
            self.game_over()

    def game_over(self):
        print(f"Game Over! Points: {self.score}")
        pygame.quit()
        exit()
