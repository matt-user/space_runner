# Class to handle the creation of levels

import pygame

import config
from enemy import Floater
from model import Model

class Level_Handler():
    def __init__(self):
        """Construct level handler."""
        self.level_one_enemy_locations = [
            (5, -10), (10, -10), (config.SCREEN_WIDTH / 2, -15),
            ((config.SCREEN_WIDTH / 2) + 3, -18), (config.SCREEN_WIDTH - 20, -15),
            (config.SCREEN_WIDTH - 40, -17), (config.SCREEN_WIDTH - 50, -10)
        ]

    def load_level(self, level):
        """Load a given level based on the level number"""
        if level == 1:
            for location in self.level_one_enemy_locations:
                new_enemy = Floater(location)
                Model.get_instance().add_enemy(new_enemy)