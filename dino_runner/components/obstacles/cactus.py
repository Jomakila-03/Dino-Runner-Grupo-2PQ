from random import randint
from dino_runner.components.obstacles.obstacle import Obstacle


class SmallCactus(Obstacle):
    def __init__(self, images):
        cactus_type = randint(0, 2)
        super().__init__(images[cactus_type])
        self.rect.y = 330

class LargeCactus(Obstacle):
    def __init__(self, images):
        cactus_type = randint(0, 2)
        super().__init__(images[cactus_type])
        self.rect.y = 300    


