from random import randint
from pygame.sprite import Sprite
from dino_runner.utils.constants import CLOUD, SCREEN_WIDTH


class Cloud(Sprite):
    def __init__(self, image=CLOUD):
        self.image = CLOUD
        self.rect = self.image.get_rect()

    def update(self, game_speed):
        self.rect.x -= game_speed
        if self.rect.x <- self.rect.width:
            self.rect.x = SCREEN_WIDTH + randint(400, 1000)
            self.rect.y = randint(80, 100)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))