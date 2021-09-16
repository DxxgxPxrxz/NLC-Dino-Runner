import pygame
import random

from nlc_dino_runner.components.obstacles.cactus import Cactus
from nlc_dino_runner.components.obstacles.bird import Bird
from nlc_dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
from nlc_dino_runner.utils.constants import CACTUS


class ObstaclesManager:
    def __init__(self):
        self.obstacles_list = []

    def update(self, game):
        if len(self.obstacles_list) == 0:
            select_cactus = random.randint(0, 1)
            if select_cactus == 0:
                cactus = Cactus(SMALL_CACTUS)
            else:
                cactus = Cactus(LARGE_CACTUS)

            bird = Bird(BIRD)
            all_obstacles_list = [cactus, bird]
            select_obstacle = all_obstacles_list[random.randint(0, 1)]
            self.obstacles_list.append(select_obstacle)

        for select_obstacle in self.obstacles_list:
            select_obstacle.update(game.game_speed, self.obstacles_list)

            if game.player.dino_rect.colliderect(select_obstacle.rect):
                pygame.time.delay(100)
            self.obstacles_list.append(Cactus(CACTUS))

        for obstacle in self.obstacles_list:
            obstacle.update(game.game_speed, self.obstacles_list)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles_list:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles_list = []
