"""This file defines the enemy class and its functionality."""

import pygame
import random
import math
import operator

import config
from animation import Animation
from projectile import Projectile
from model import Model

# TODO: make factory for enemies

# Enemy class that tries to destroy user
class Enemy(pygame.sprite.Sprite):
	def __init__(self, speed):
		super().__init__()
		self.speed = speed
		self.moving = False
		self.delta = (0, 0)

	# remove the sprite when it passes the bottom edge of the screen
	def update(self):
		"""Update the behavior of enemy."""
		if self.moving:
			self.update_location()
		if self.rect.top > config.SCREEN_HEIGHT:
			self.kill()
	
	def start_moving(self, point):
		"""Tells this object to start moving to the point."""
		if (self.rect.x, self.rect.y) == point:
			if self.moving:
				self.stop_moving()
			return
		self.moving = True
		self.destination = point
		self.compute_delta()
	
	def compute_delta(self):
		"""Compute the change in the x and y direction for each update"""
		x_dir, y_dir = self.get_direction_from_self(self.destination)
		self.delta = (x_dir * self.speed, y_dir * self.speed)

	def stop_moving(self):
		"""Tells this object to stop moving"""
		self.moving = False
		self.destination = None

	def update_location(self):
		"""Update the location of the enemy."""
		# if the difference between the destination and the enemy 
		# is small enough consider us at the destination
		if self.is_enemy_at_location(self.destination):
			self.stop_moving()
			return True
		x_dir, y_dir = self.get_direction_from_self(self.destination)
		self.rect.move_ip(self.speed * x_dir, self.speed * y_dir)
		return False
	
	def get_direction_from_self(self, point):
		"""Returns the normalized direction from the enemy to the point."""
		x_dif, y_dif = map(operator.sub, point, self.get_enemy_gun())
		magnitude = math.sqrt(x_dif ** 2 + y_dif ** 2)
		x_dif_normed = x_dif / magnitude
		y_dif_normed = y_dif / magnitude
		return x_dif_normed, y_dif_normed

	def get_enemy_gun(self):
		"""Returns the position of the enemy's gun"""
		return (
			self.rect.x + (self.surf.get_width() / 2),
			self.rect.y + self.surf.get_height()
		)

	def is_enemy_at_location(self, point):
		"""Returns whether the enemy is at the given point."""
		x_dif, y_dif = map(operator.sub, point, self.get_enemy_gun())
		return (abs(x_dif) <= self.delta[0]) and (abs(y_dif) <= self.delta[1])

	def is_moving(self):
		"""Return whether the enemy is moving."""
		return self.moving
		

class Mall_Fighter(Enemy):
	"""Mall Fighter class that inherits from the Enemy base."""

	# class constants
	MALL_FIGHTER_SPEED = 3

	def __init__(self, center, waypoints, firepoints):
		"""Constructs the mall fighter at center=center"""
		super().__init__(Mall_Fighter.MALL_FIGHTER_SPEED)
		self.fire_idx = 0
		self.way_idx = 0
		self.waypoints = waypoints
		self.firepoints = firepoints
		self.surf = pygame.Surface((50, 50))
		self.surf.fill((255, 255, 255))
		self.rect = self.surf.get_rect(center=center)
	
	def update(self):
		"""Update the behavior of the Mall Fighter."""
		Enemy.update(self)
		if self.way_idx < len(self.waypoints) and not Enemy.is_moving(self):
			Enemy.start_moving(self, self.waypoints[self.way_idx])
			self.way_idx += 1
		if self.fire_idx < len(self.firepoints) and Enemy.is_enemy_at_location(self, self.firepoints[self.fire_idx]):
			self.fire_at_player()
			self.fire_idx += 1

	def fire_at_player(self):
		"""Fire a projectile at the player."""
		new_projectile = Projectile(
			center=self.get_enemy_gun(),
			direction=Enemy.get_direction_from_self(self, Model.get_instance().get_player_gun())
		)
		Model.get_instance().add_enemy_projectile(new_projectile)


# Float enemy that inherits from enemy
# this enemy simply floats down the screen
class Floater(Enemy):
	# Minimum and maximum possible speeds for this enemy
	MIN_SPEED_POSSIBLE = 2
	MAX_SPEED_POSSIBLE = 3
	ANIMATION_DELAY = 10
	FLOATER_SPEED = 2

	def __init__(self, center):
		super().__init__(Floater.FLOATER_SPEED)
		# load all of the floater's animations
		self.animation = Animation(Floater.ANIMATION_DELAY, 'assets', 'enemy')
		self.surf = self.animation.get_image()
		self.rect = self.surf.get_rect(center=center)
		self.speed = Floater.FLOATER_SPEED
	
	def update(self):
		"""Update the behavior of a Floater enemy."""
		self.surf = self.animation.next_animation()
		self.rect.move_ip(0, self.speed)
		Enemy.update(self)
	