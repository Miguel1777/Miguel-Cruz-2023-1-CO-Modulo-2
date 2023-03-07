import pygame

from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import LargeCactus
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.utils.constants import LARGE_CACTUS
from dino_runner.utils.constants import BIRD



class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            cactus = Cactus(SMALL_CACTUS)
            large_cactus = LargeCactus(LARGE_CACTUS)
            bird = Bird(BIRD)
            self.obstacles.append(bird)
            self.obstacles.append(large_cactus)
            self.obstacles.append(cactus)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            
            if game.player.dino_rect.colliderect(obstacle.rect):
                #pygame.time.delay(1000)
                game.playing = False
                break 

    def draw(self, screen):
        for obstacle in self.obstacles: 
            obstacle.draw(screen)
        