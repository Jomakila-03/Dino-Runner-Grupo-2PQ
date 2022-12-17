from random import randint
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import HEART


class Heart(Obstacle):
    def __init__(self, HEART):
        super().__init__(HEART)
        self.rect.y = randint(200,300)

# heart es un obstaculo, no da vidas 
