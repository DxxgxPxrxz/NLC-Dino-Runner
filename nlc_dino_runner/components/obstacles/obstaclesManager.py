import random

import pygame.time
from nlc_dino_runner.components.obstacles.bird import Bird
from nlc_dino_runner.components.obstacles.cactus import Cactus
from nlc_dino_runner.utils.constants import CACTUS, BIRD, HIT_SOUND, GAME_OVER_SOUND #AÑADIDO



class ObstaclesManager:
    def __init__(self):
        self.obstacles_list = []

    def update(self, game, screen):
        if len(self.obstacles_list) == 0:
            if random.randint(0, 1) == 0:
                self.obstacles_list.append(Cactus(CACTUS))
            elif random.randint(0, 1) == 1:
                self.obstacles_list.append(Bird(BIRD))

        for obstacle in self.obstacles_list:
            obstacle.update(game.game_speed, self.obstacles_list)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.shield:
                    self.obstacles_list.remove(obstacle)
                else:
                    if game.live_manager.lives > 1:
                        HIT_SOUND.play() #AÑADIDO
                        game.live_manager.reduce_lives()
                        game.player.shield = True
                        start_time = pygame.time.get_ticks()
                        game.player.shield_time_up = start_time + 1000

                    else:
                        game.player.draw_dead(screen)
                        pygame.time.delay(500)
                        game.playing = False
                        GAME_OVER_SOUND.play()
                        game.death_count += 1
                        break
            elif game.player.hammer and game.player.hammer.rect.colliderect(obstacle.rect):#AÑADIDO
                self.obstacles_list.remove(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles_list:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles_list = []