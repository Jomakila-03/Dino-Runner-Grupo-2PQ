import pygame

from dino_runner.utils.constants import FONT_STYLE
from dino_runner.utils.message import message_draw



class Score:
    def __init__(self):
        self.points = 0

    def update(self, game):
        self.points += 1
        if self.points % 100 == 0:
            game.game_speed += 2

    def draw(self, screen):
        message_draw(
            f"Score: {self.points}",
            screen,
            font_size=22,
            pos_x_center=1000,
            pos_y_center=40,
        )
    
    def reset_score(self):
        self.points = 0

        