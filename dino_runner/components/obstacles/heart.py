from random import randint
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import HEART, SCREEN_WIDTH


class Heart(Obstacle):
    def __init__(self, image=HEART):
        self.image = HEART
        self.rect = self.image.get_rect() 
        self.rect.y=  randint(120, 350)
        self.step = 0

    def update(self, image):
        if self.step >=9:
            self.step = 0
        self.step += 1

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        screen.blit(HEART, self.rect)