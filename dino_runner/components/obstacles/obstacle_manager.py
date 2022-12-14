from random import randint
import pygame
from dino_runner.components.obstacles.bird import Bird_Two, Bird_one
from dino_runner.components.obstacles.cactus import LargeCactus, SmallCactus
from dino_runner.utils.constants import BIRD, LARGE_CACTUS, SMALL_CACTUS

class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            if randint(0, 2):
                self.obstacles.append(SmallCactus(SMALL_CACTUS))
            elif randint(0, 2):
                self.obstacles.append(LargeCactus(LARGE_CACTUS)) 
            elif randint(0, 1):
                    self.obstacles.append(Bird_one(BIRD))
            elif randint(0, 1):
                self.obstacles.append(Bird_Two(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if obstacle.rect.colliderect(game.player.rect):
                pygame.time.delay(1000)
                game.playing = False

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    