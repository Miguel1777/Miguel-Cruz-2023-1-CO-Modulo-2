import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

POSICIONES_INICIALES = [(1300, 280), (1300, 350), (1300, 295)]

class Bird(Obstacle):
    def __init__(self, image):
        obstacle_type = 1
        super().__init__(BIRD, 1)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = random.choice(POSICIONES_INICIALES)

        