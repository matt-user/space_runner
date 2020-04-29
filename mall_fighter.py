"""Mall fighter class that inherits from enemy."""

from enemy import Enemy
from animation import Animation
from projectile import Projectile
from model import Model
from utility import get_direction

class Mall_Fighter(Enemy):

    # class constant
    MALL_FIGHTER_SPEED = 3
    ANIMATION_DELAY = 30
    GUN_POS_OFFSETS = [(15, 50), (35, 50)]
    # a list of folders that specify the filepath to the animation images
    FILE_PATH = ['assets', 'enemy', 'mall_fighter']

    def __init__(self, center, waypoints, firepoints):
        """Constructs the mall fighter at center=center"""
        super().__init__(center, Mall_Fighter.MALL_FIGHTER_SPEED, Mall_Fighter.ANIMATION_DELAY, *Mall_Fighter.FILE_PATH)
        self.fire_idx = 0
        self.way_idx = 0
        self.waypoints = waypoints
        self.firepoints = firepoints
    
    def update(self):
        """Update the behavior of the Mall Fighter."""
        Enemy.update(self)
        self.update_movement()
        self.update_firing()
        self.surf = self.animation.next_animation()

    def update_movement(self):
        """Updates the mall fighters movement"""
        if self.way_idx < len(self.waypoints) and not self.moving_object.is_moving:
            self.moving_object.start_moving(self.waypoints[self.way_idx])
            self.way_idx += 1

    def update_firing(self):
        """Updates the mall fighters firing"""
        if (self.fire_idx < len(self.firepoints) and
            self.moving_object.is_at_location(self.firepoints[self.fire_idx])):
            self.fire_at_player()
            self.fire_idx += 1

    def fire_at_player(self):
        """Fire a projectile at the player."""
        play_center = Model.get_instance().get_player_center()
        for gun_pos in self.get_enemy_gun():
            direct = get_direction(gun_pos, play_center)
            new_projectile = Projectile(
                center=gun_pos,
                direction=direct
            )
            Model.get_instance().add_enemy_projectile(new_projectile)

    def get_enemy_gun(self):
        """Returns the point(s) of the enemy's gun(s)"""
        return [(self.rect.x + x_pos, self.rect.y + y_pos) for x_pos, y_pos in Mall_Fighter.GUN_POS_OFFSETS]
    