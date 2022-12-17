from random import randint

import pygame
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.heart import Heart
from dino_runner.utils.constants import  BIRD, HEART, LARGE_CACTUS, SMALL_CACTUS


class ObstacleManager:
    SMALL_CACTUS_Y_POS = 330
    LARGE_CACTUS_Y_POS = 300

    def __init__(self):
        self.obstacles = []

    def obstacle(self):
        object_random = randint(0, 3)

        if object_random == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS, self.SMALL_CACTUS_Y_POS))
        elif object_random == 1:
            self.obstacles.append(Cactus(LARGE_CACTUS, self.LARGE_CACTUS_Y_POS))
        elif object_random == 2:
            self.obstacles.append(Heart(HEART))
        else:
            self.obstacles.append(Bird(BIRD))

    def update(self, game_speed, player, on_death):
        if len(self.obstacles) == 0:
            self.obstacle()
 
        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if obstacle.rect.colliderect(player.rect) and on_death():
                pygame.time.delay(2000)
              
   
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
    def reset_obstacles(self):
        self.obstacles = []