import os
import math
import pygame

import config

from utility import get_image
from animation import Animation

# Projectile class that destroys entities
class Projectile(pygame.sprite.Sprite):
	# class constants
	ANIMATION_DELAY = 20

	def __init__(self, center, direction=(0, -1)):
		super().__init__()
		self.speed = 6
		self.x_dir, self.y_dir = direction
		self.x_dir *= self.speed
		self.y_dir *= self.speed
		# load all of the projectile animations
		rotation_angle = self.get_rotation_angle()
		self.animation = Animation(Projectile.ANIMATION_DELAY, 'assets', 'projectile')
		self.animation.rotate_center(rotation_angle)
		self.surf = self.animation.get_image()
		self.rect = self.surf.get_rect(center=center)
	
	def update(self):
		"""update the projectile's location"""
		self.surf = self.animation.next_animation()
		self.rect.move_ip(self.x_dir, self.y_dir)
		self.check_projectile_bounds()
	
	def check_projectile_bounds(self):
		"""Check the projectile bounds."""
		# remove the sprite when it passes the edges of the screen
		if (self.rect.bottom < 0 or self.rect.top > config.SCREEN_HEIGHT
			or self.rect.right < 0 or self.rect.left > config.SCREEN_WIDTH):
			self.kill()
	
	def get_rotation_angle(self):
		"""Returns the rotation angle of the projectile."""
		rotation_angle = math.atan(self.x_dir / self.y_dir) * (180.0 / math.pi)
		# flip rotation if y_dir is positive
		if self.y_dir > 0:
			rotation_angle += 180
		return rotation_angle