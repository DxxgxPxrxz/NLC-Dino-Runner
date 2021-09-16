import random

from nlc_dino_runner.components.obstacles.obstacles import Obstacles


# Clase hija
class Cactus(Obstacles):
    def __init__(self, image):
        self.type = random.randint(0, 5)
        super().__init__(image, self.type)


        self.rect.y = 330
        if self.type > 2:
            self.rect.y = 300
        else:
            self.rect.y = 320
