import os
import pygame

from utility import get_image
from animation import Animation

# Projectile class that destroys entities
class Projectile(pygame.sprite.Sprite):
	# class constants
	ANIMATION_DELAY = 20

	def __init__(self, center):
		super().__init__()
		# load all of the projectile animations
		self.animation = Animation(Projectile.ANIMATION_DELAY, 'assets', 'projectile')
		self.surf = self.animation.get_image()
		self.rect = self.surf.get_rect(center=center)
	
	def update(self):
		"""update the projectile's location"""
		self.surf = self.animation.next_animation()
		self.rect.move_ip(0, -3)
		self.check_projectile_bounds()
	
	def check_projectile_bounds(self):
		"""Check the projectile bounds."""
		# remove the sprite when it passes the top edge of the screen
		if self.rect.bottom < 0:
			self.kill()