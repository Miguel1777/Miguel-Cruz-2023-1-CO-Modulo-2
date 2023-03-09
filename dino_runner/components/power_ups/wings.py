from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import WINGS, WINGS_TYPE

class Wings(PowerUp):
    def __init__(self, type):
        super().__init__(WINGS, WINGS_TYPE)
        self.type = WINGS_TYPE
