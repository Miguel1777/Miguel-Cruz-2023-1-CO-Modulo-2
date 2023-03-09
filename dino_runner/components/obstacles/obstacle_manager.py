import pygame
import random

from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import LargeCactus
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.utils.constants import LARGE_CACTUS
from dino_runner.utils.constants import BIRD
from dino_runner.utils.constants import SHIELD_TYPE



class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            type = random.randint(0,2)

            if type == 0:
                cactus = Cactus(SMALL_CACTUS)
                self.obstacles.append(cactus)

            elif type == 1:
                large_cactus = LargeCactus(LARGE_CACTUS)
                self.obstacles.append(large_cactus) 

            elif type == 2:
                bird = Bird(BIRD) 
                self.obstacles.append(bird)


        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.type != SHIELD_TYPE:
                  game.death_count += 1 
                  game.playing = False
                  break
            #else:
                #self.obstacles.remove(obstacle) 

    def draw(self, screen):
        for obstacle in self.obstacles: 
            obstacle.draw(screen)


    def reset_obstacles(self):
        self.obstacles = []
        