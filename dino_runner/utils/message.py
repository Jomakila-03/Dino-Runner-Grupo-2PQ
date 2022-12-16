import pygame

from dino_runner.utils.constants import HALF_SCREEN_HEIGHT, HALF_SCREEN_WIGTH


FONT_COLOR = (255, 255, 255)
FONT_SIZE = 30
FONT_STYLE = "freesansbold.ttf"

def message_draw(
    message,
    screen, 
    font_color = FONT_COLOR,
    font_size = FONT_SIZE,
    pos_y_center = HALF_SCREEN_HEIGHT,
    pos_x_center = HALF_SCREEN_WIGTH,
):
    font = pygame.font.Font(FONT_STYLE, font_size)
    txt = font.render(message, True, font_color)
    txt_rect = txt.get_rect()
    txt_rect.center = (pos_x_center, pos_y_center)
    screen.blit(txt, txt_rect)