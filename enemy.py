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

	def stop_moving(self):
		"""Tells this object to stop moving"""
		self.moving = False
		self.destination = None

	def update_location(self):
		"""Update the location of the enemy."""
		if (self.get_enemy_gun()) == self.destination:
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
		

class Mall_Fighter(Enemy):
	"""Mall Fighter class that inherits from the Enemy base."""

	# class constants
	MALL_FIGHTER_SPEED = 3

	def __init__(self, center):
		"""Constructs the mall fighter at center=center"""
		super().__init__(Mall_Fighter.MALL_FIGHTER_SPEED)
		# self.stop_pos = stop_pos
		# self.move_dir = move_dir
		self.counter = 0
		self.surf = pygame.Surface((50, 50))
		self.surf.fill((255, 255, 255))
		self.rect = self.surf.get_rect(center=center)
	
	def update(self):
		"""Update the behavior of the Mall Fighter."""
		Enemy.update(self)
		self.counter += 1
		if self.counter == 15:
			self.counter = 0
			self.fire_at_player()

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
	