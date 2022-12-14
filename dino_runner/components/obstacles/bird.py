
from random import randint
from dino_runner.components.obstacles.obstacle import Obstacle


class Bird_one(Obstacle):
    def __init__(self, images):
        bird_type = randint(0, 1)
        super().__init__(images[bird_type])
        self.rect.y = 250

class Bird_Two(Obstacle):
    def __init__(self, images):
        bird_type = randint(0, 1) 
        super().__init__(images[bird_type])
        self.rect.y = 320