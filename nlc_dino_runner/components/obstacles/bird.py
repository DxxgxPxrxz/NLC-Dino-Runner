import random

from nlc_dino_runner.components.obstacles.obstacles import Obstacles
from nlc_dino_runner.utils.constants import BIRD


# Clase hija
class Bird(Obstacles):
    position_y_list = [230, 270, 330]

    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.step_index = 0
        self.rect.y = self.position_y_list[random.randint(0, 2)]

    def draw(self, screen):
        if self.step_index >= 20:
            self.step_index = 0

        self.image = BIRD[0] if self.step_index < 10 else BIRD[1]
        screen.blit(self.image, self.rect)
        self.step_index += 1
