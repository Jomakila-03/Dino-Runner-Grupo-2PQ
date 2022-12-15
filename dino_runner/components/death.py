import pygame

from dino_runner.utils.constants import FONT_STYLE

class Death:
    def __init__(self):
        self.death_count = 0

    def update(self):
        self.death_count += 1
        if self.death_count == self.score: 
            self.death_count.reset()
           


    def draw(self, screen):
        font = pygame.font.Font(FONT_STYLE, 22)
        message = font.render(f"Death count: {self.death_count}", True, (255, 255, 255), (255, 0, 0))
        message_rect = message.get_rect()
        message_rect.center = (1000, 40)
        screen.blit(message, message_rect)