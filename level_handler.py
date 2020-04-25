# Class to handle the creation of levels

import pygame

import config
from enemy import Floater
from enemy import Mall_Fighter
from model import Model

class Level_Handler():
    def __init__(self):
        """Construct level handler."""
        """self.level_one_enemy_locations = [
            (10, -10), (50, -50), (config.SCREEN_WIDTH / 2, -900),
            ((config.SCREEN_WIDTH / 2) - 30, -1000), ((config.SCREEN_WIDTH / 2) + 50, -1100)
        ]"""
        self.level_one_enemy_locations = [
            (config.SCREEN_WIDTH / 2, 0)
        ]

    def load_level(self, level):
        """Load a given level based on the level number"""
        if level == 1:
            for location in self.level_one_enemy_locations:
                new_enemy = Mall_Fighter(location)
                Model.get_instance().add_enemy(new_enemy)