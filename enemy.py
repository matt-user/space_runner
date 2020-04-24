"""This file defines the enemy class and its functionality."""

import pygame
import random

import config
from animation import Animation

# Enemy class that tries to destroy user
class Enemy(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()

	# remove the sprite when it passes the bottom edge of the screen
	def update(self):
		"""Update the behavior of enemy."""
		if self.rect.top > config.SCREEN_HEIGHT:
			self.kill()

# Float enemy that inherits from enemy
# this enemy simply floats down the screen
class Floater(Enemy):
	# Minimum and maximum possible speeds for this enemy
	MIN_SPEED_POSSIBLE = 3
	MAX_SPEED_POSSIBLE = 5
	ANIMATION_DELAY = 10

	def __init__(self, center):
		super().__init__()
		# load all of the floater's animations
		self.animation = Animation(Floater.ANIMATION_DELAY, 'assets', 'enemy')
		self.surf = self.animation.get_image()
		self.rect = self.surf.get_rect(center=center)
		self.speed = random.randint(Floater.MIN_SPEED_POSSIBLE, Floater.MAX_SPEED_POSSIBLE)
	
	def update(self):
		"""Update the behavior of a Floater enemy."""
		self.surf = self.animation.next_animation()
		self.rect.move_ip(0, self.speed)
		Enemy.update(self)
	