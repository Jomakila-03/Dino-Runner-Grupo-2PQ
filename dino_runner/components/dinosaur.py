import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import DEFAULT_TYPE, DINO_DEAD, DUCKING_HAMMER, DUCKING_SHIELD, HAMMER_TYPE, JUMPING, JUMPING_SHIELD, RUNNING, DUCKING, RUNNING_SHIELD, SHIELD_TYPE, SOUND_DEAD, SOUND_JUMP, SOUND_POWER
from dino_runner.utils.message import message_draw
JUMPING_ACTION = "jumping"
RUNNING_ACTION = "running"
DUCKING_ACTION = "ducking"
HAMMER_ACTION = "hamming"
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD}
DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD}
HAMM_IMG = {DEFAULT_TYPE: DUCKING_HAMMER, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}

pygame.mixer.init()

class Dinosaur(Sprite):
    Y_POS = 310
    X_POS = 80
    Y_POS_DUCK = 340
    JUMP_VELOCITY = 8.5
 
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.reset_rect()
        self.jump_velocity = self.JUMP_VELOCITY
        self.step = 0
        self.action = RUNNING_ACTION
        self.has_power_up = False
        self.power_up_time_up = 0
        self.life = 3 
    
    def reset_rect(self, y_pos=None):
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = y_pos or self.Y_POS

    def update(self, user_input):
        if self.action == RUNNING_ACTION:
            self.run()
        elif self.action == JUMPING_ACTION:
            self.jump()  
            SOUND_JUMP.play()
        elif self.action == DUCKING_ACTION:
            self.duck()
        elif self.action == HAMMER_ACTION:
            self.ducking_hammer()

        if self.action != JUMPING_ACTION:
            if user_input[pygame.K_UP]:
                self.action = JUMPING_ACTION
            elif user_input[pygame.K_DOWN]:
                self.action = DUCKING_ACTION
            elif user_input[pygame.K_RIGHT]:
                self.action = HAMMER_ACTION
            else:
                self.action = RUNNING_ACTION

        if self.step >= 9:
            self.step = 0

    def run(self):
        self.image = RUN_IMG[self.type][self.step // 5]
        self.reset_rect()
        self.step += 1
    
    def jump(self):
        self.image = JUMP_IMG[self.type]
        y_pos = self.rect.y - self.jump_velocity * 4
        self.reset_rect(y_pos=y_pos)
        self.jump_velocity -= 0.8
        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.reset_rect()
            self.jump_velocity = self.JUMP_VELOCITY
            self.action = RUNNING_ACTION

    def duck(self):
        self.image = DUCK_IMG[self.type][self.step // 5] 
        self.reset_rect(y_pos=self.Y_POS_DUCK)
        self.step += 1

    def ducking_hammer(self):
        self.image = HAMM_IMG[self.type][self.step // 5]
        self.reset_rect(y_pos=self.Y_POS_DUCK)
        self.step +=1
        
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def on_pick_power_up(self, power_up):
        self.has_power_up = True
        self.power_up_time_up = power_up.start_time + (power_up.duration * 1000)
        self.type = power_up.type 
        SOUND_POWER.play()

    def draw_active_power_up(self, screen):
        if self.has_power_up:
            left_time = round((self.power_up_time_up - pygame.time.get_ticks()) / 1000,2)
            if left_time >=0:
                message_draw(
                    f"{self.type.capitalize()} enabled for {left_time} seconds.",
                    screen,
                    font_size=18,
                    pos_y_center=40,
                )
            else:
                self.type = DEFAULT_TYPE
                self.has_power_up = False

    def on_dino_death(self):
        self.image = DINO_DEAD
        SOUND_DEAD.play()


    
 




