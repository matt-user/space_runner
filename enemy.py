"""This file defines the enemy class and its functionality."""

import pygame
import random
import math
import operator

import config
from animation import Animation
from projectile import Projectile
from model import Model
from utility import get_direction
from moving_object import Moving_Object

# TODO: make factory for enemies

# Enemy class that tries to destroy user
class Enemy(pygame.sprite.Sprite):
	def __init__(self, center, speed, animation_delay, *filepath):
		super().__init__()
		self.animation = Animation(animation_delay, *filepath)
		self.surf = self.animation.get_image()
		self.rect = self.surf.get_rect(center=center)
		self.moving_object = Moving_Object(speed, self.rect)

	# remove the sprite when it passes the bottom edge of the screen
	def update(self):
		"""Update the behavior of enemy."""
		self.surf = self.animation.next_animation()
		if self.moving_object.is_moving:
			self.moving_object.update_location()
		self.check_enemy_bounds()
	
	def check_enemy_bounds(self):
		"""If the enemy is off of the screen kill it."""
		# we don't check if the enemy is off the top bc that is were they spawn
		# could add a bool to see if enemy was on the screen then off
		if (self.rect.top > config.SCREEN_HEIGHT or self.rect.left > config.SCREEN_WIDTH
			or self.rect.right < 0):
			self.kill()
	
