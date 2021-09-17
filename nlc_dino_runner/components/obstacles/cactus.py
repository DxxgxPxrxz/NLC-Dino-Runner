import random

from nlc_dino_runner.components.obstacles.Obstacles import Obstacles


class Cactus(Obstacles):
    def __init__(self, image):
        self.type = random.randint(0, 5)
        super().__init__(image, self.type)
        if self.type > 2:
            self.rect.y = 305
        else:
            self.rect.y = 320





