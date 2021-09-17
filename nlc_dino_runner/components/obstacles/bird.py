import random
from nlc_dino_runner.components.obstacles.obstacles import Obstacles

class Bird(Obstacles):

    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.index = 0
        if random.randint(0, 1) == 0:
            self.rect.y = 250
        if random.randint(0, 1) == 1:
            self.rect.y = 200

    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
        screen.blit(self.image[self.index//5], self.rect)
        self.index += 1