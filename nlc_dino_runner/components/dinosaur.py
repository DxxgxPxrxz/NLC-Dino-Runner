import pygame
from pygame.sprite import Sprite

from nlc_dino_runner.components.hammer import Hammer
from nlc_dino_runner.utils import text_utils
from nlc_dino_runner.utils.constants import (
    RUNNING,
    DUCKING,
    JUMPING,
    HAMMER,
    RUNNING_SHIELD,
    DUCKING_SHIELD,
    JUMPING_SHIELD,
    RUNNING_HAMMER, #AÑADIDO
    DUCKING_HAMMER, #AÑADIDO
    JUMPING_HAMMER, #AÑADIDO
    DEFAULT_TYPE,
    SHIELD_TYPE,
    HAMMER_TYPE,#AÑADIDO
    DINO_DEAD#AÑADIDO
)

class Dinosaur(Sprite):

    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8

    def __init__(self):
        self.run_img = {
            DEFAULT_TYPE: RUNNING,
            SHIELD_TYPE: RUNNING_SHIELD,
            HAMMER_TYPE: RUNNING_HAMMER #AÑADIDO
        }
        self.jump_img = {
            DEFAULT_TYPE: JUMPING,
            SHIELD_TYPE: JUMPING_SHIELD,
            HAMMER_TYPE: JUMPING_HAMMER #AÑADIDO
        }
        self.duck_img = {
            DEFAULT_TYPE: DUCKING,
            SHIELD_TYPE: DUCKING_SHIELD,
            HAMMER_TYPE: DUCKING_HAMMER #AÑADIDO
        }
        self.type = DEFAULT_TYPE
        self.image = self.run_img[self.type][0]
        self.hammer_image = HAMMER
        self.dead_img = DINO_DEAD

        self.shield = False
        self.shield_time_up = 0
        self.show_text = False


        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.jump_vel = self.JUMP_VEL

        self.hammer = None #AÑADIDO
        self.hammer_available = False
        self.hammer_time_up = 0
        self.show_hammer_text = False
        self.hammer_availables = 0


    def update(self, user_input):
        if self.dino_jump:
            self.jump()
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()

        if user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_jump = False
            self.dino_run = False
        elif user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_duck = False
            self.dino_run = False
        elif not self.dino_jump:
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False


        if user_input[pygame.K_SPACE] and self.hammer_available:
            self.hammer = Hammer(self.dino_rect.x, self.dino_rect.y)
            self.hammer_availables += 1
            if self.hammer_availables == 8:
                self.hammer_available = False
                self.type = DEFAULT_TYPE
                self.hammer_availables = 0

        if self.hammer:
            self.hammer.update()


        if self.step_index >= 10:
            self.step_index = 0

    def run(self):
        self.image = self.run_img[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def duck(self):
        self.image = self.duck_img[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def check_invincibility(self, screen):
        if self.shield:
            time_to_show = round((self.shield_time_up - pygame.time.get_ticks()) / 1000, 2)
            #0.24
            if time_to_show < 0:
                self.shield = False
                if self.type == SHIELD_TYPE: #or self.type == HAMMER_TYPE: #AÑADIDO VOLVER A DEFAULT TYPE EN POWERUPS
                    self.type = DEFAULT_TYPE
            else: #AÑADIDO CONDICIONAL ADICIONAL PARA EL TEXT DE HAMMER
                if self.show_text and self.type == SHIELD_TYPE:
                    text, text_rect = text_utils.get_centered_message(
                        f'Shield enabled for {time_to_show} seg',
                        width=500,
                        height=40,
                        size=20
                    )
                    screen.blit(text, text_rect)
                else:
                    text, text_rect = text_utils.get_centered_message(
                        f'Invincibility enabled for {time_to_show} seg',
                        width=500,
                        height=100,
                        size=20
                    )
                    screen.blit(text, text_rect)


    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
        if self.hammer:
            self.hammer.draw(screen)

    def draw_dead(self, screen):
        self.image = self.dead_img
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


#Clase 3: Dino