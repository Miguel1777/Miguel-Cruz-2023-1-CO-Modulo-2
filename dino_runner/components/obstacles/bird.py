import random
import pygame

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

POSICIONES_INICIALES = [(1300, 220), (1300, 320), (1300, 250)]

class Bird(Obstacle):
    def __init__(self, image):
        obstacle_type = 1
        super().__init__(BIRD, 1)
        self.rect = self.image[0].get_rect()
        self.rect.x, self.rect.y = random.choice(POSICIONES_INICIALES)
        self.fligth = 0
        

    def draw(self, screen):
        if self.fligth >= 9:
            self.fligth = 0
        screen.blit(self.image[self.fligth//5], self.rect)
        self.fligth += 1