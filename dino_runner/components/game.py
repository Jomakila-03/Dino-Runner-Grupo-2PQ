import pygame
from dino_runner.components.cloud import Cloud
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.heart import Heart
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.score import Score
from dino_runner.utils.constants import (
    BG,
    DINO_START,
    HALF_SCREEN_HEIGHT,
    HALF_SCREEN_WIGTH,
    ICON,
    INITIAL_GAME_VELOCITY,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    SHIELD_TYPE,
    TITLE,
    FPS,
)
from dino_runner.utils.message import message_draw

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = INITIAL_GAME_VELOCITY
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.score = Score()
        self.cloud = Cloud()
        self.heart = Heart()
        self.death_count = 0
        self.lives = 3
        self.executing = False

    def execute(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.show_menu()

        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.reset_game()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def reset_game(self):
        self.playing = True
        self.game_speed = INITIAL_GAME_VELOCITY
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.score.reset_score()
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self.game_speed, self.player, self.on_death)
        self.power_up_manager.update(self.game_speed, self.score.points, self.player)
        self.score.update(self)
        self.heart.update(self)
        self.cloud.update(self.game_speed)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((204, 153, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.player.draw_active_power_up(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.score.draw(self.screen)
        self.heart.draw(self.screen)
        self.cloud.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def show_menu(self):
        self.screen.fill((204, 153, 255))
        if self.death_count == 0:
            message_draw("Press any key to start", self.screen)
        else:
            message_draw(
            "GAME_OVER", self.screen, font_size=50, pos_y_center=HALF_SCREEN_HEIGHT -150
            )
            message_draw("Press any key to restart", self.screen)
            message_draw(
                f"Your score: {self.score.points}",
                self.screen,
                font_size=24,
                pos_y_center=HALF_SCREEN_HEIGHT +30,
            )

            message_draw(
                f"Death count: {self.death_count}",
                self.screen,
                font_size=24,
                pos_y_center=HALF_SCREEN_HEIGHT +60,
            )
        
        if self.lives == 3:
            message_draw(
                f"You have {self.lives} lives",
                self.screen,
                font_size = 15,
                pos_y_center=HALF_SCREEN_HEIGHT +90,
                )

       

        self.screen.blit(DINO_START, (HALF_SCREEN_WIGTH -40, HALF_SCREEN_HEIGHT-120))
        pygame.display.update()
        self.handle_menu_events()

    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.executing = False
            elif event.type == pygame.KEYDOWN:
                self.run()
    
    def on_death(self):
        has_shield = self.player.type == SHIELD_TYPE
        if not has_shield:
            self.player.on_dino_death()
            self.draw()
            self.death_count += 1
  
            self.playing = False
        
        return not has_shield

    def lives(self):
        for self.live in range(1, self.lives==3):
            if self.player.live == 1:
                self.playing = False
   



        


                    
                





