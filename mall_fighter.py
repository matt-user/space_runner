"""Mall fighter class that inherits from enemy."""

from enemy import Enemy
from animation import Animation
from projectile import Projectile
from model import Model

class Mall_Fighter(Enemy):

	# class constants
	MALL_FIGHTER_SPEED = 3
	ANIMATION_DELAY = 30
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
		if self.way_idx < len(self.waypoints) and not Enemy.is_moving(self):
			Enemy.start_moving(self, self.waypoints[self.way_idx])
			self.way_idx += 1
		if self.fire_idx < len(self.firepoints) and Enemy.is_enemy_at_location(self, self.firepoints[self.fire_idx]):
			self.fire_at_player()
			self.fire_idx += 1
		self.surf = self.animation.next_animation()

	def fire_at_player(self):
		"""Fire a projectile at the player."""
		new_projectile = Projectile(
			center=self.get_enemy_gun(),
			direction=Enemy.get_direction_from_self(self, Model.get_instance().get_player_gun())
		)
		Model.get_instance().add_enemy_projectile(new_projectile)
	