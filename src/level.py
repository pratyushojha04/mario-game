import pygame
import random
import json
from game_plateform import Platform
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Level:
    def __init__(self, level_file):
        self.platforms = pygame.sprite.Group()
        self.time_elapsed = 0
        self.score = 0  # Initialize score
        self.load_level(level_file)

    def load_level(self, level_file):
        with open(level_file) as f:
            platform_data = json.load(f)["platforms"]

        for data in platform_data:
            x = random.randint(0, SCREEN_WIDTH - data["width"])
            y = random.randint(-200, -50)  # Start above the screen
            platform = Platform(x, y, data["width"], data["height"], data["speed"])
            self.platforms.add(platform)

    def update(self):
        self.time_elapsed += 1
        for platform in self.platforms:
            platform.speed = 5 + self.time_elapsed // 100  # Increase speed over time
        self.platforms.update()
        
        # Update score based on time or other game mechanics
        self.score = self.time_elapsed // 10  # Example scoring mechanism

    def draw(self, screen):
        self.platforms.draw(screen)
        # Draw the score on the screen
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f'Score: {self.score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))  # Position of the score on the screen
