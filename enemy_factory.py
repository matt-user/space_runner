"""File is resposible for the construction of enemies."""

from floater import Floater
from mall_fighter import MallFighter

def create_enemy(location, enemy_type, waypoints, firepoints):
    """Creates and returns an enemy specified"""
    if enemy_type == "Floater":
        return Floater(location)
    elif enemy_type == "Mall_Fighter":
        return MallFighter(location, waypoints, firepoints)