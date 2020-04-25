import os
import pygame
import config
from utility import get_image
from animation import Animation

from pygame.locals import (
	K_w,
	K_s,
	K_a,
	K_d
)

# Player class that user controls
class Player(pygame.sprite.Sprite):
	# class constants
	ANIMATION_DELAY = 10
	X_SPEED = 3
	Y_SPEED = 3

	def __init__(self):
		super().__init__()
		# load all of the players animations
		self.animation = Animation(Player.ANIMATION_DELAY, 'assets', 'player')
		self.surf = self.animation.get_image()
		self.rect = self.surf.get_rect(
			center=(
				config.SCREEN_WIDTH / 2, config.SCREEN_HEIGHT
			)
		)


	def update(self, pressed_keys):
		"""Updates all of the player's information"""
		self.surf = self.animation.next_animation()
		self.update_movement(pressed_keys)


	def update_movement(self, pressed_keys):
		"""Update player movement based on pressed keys"""
		# update the players movement based on the pressed keys
		if pressed_keys[K_w]:
			self.rect.move_ip(0, -Player.X_SPEED)
		if pressed_keys[K_s]:
			self.rect.move_ip(0, Player.X_SPEED)
		if pressed_keys[K_a]:
			self.rect.move_ip(-Player.Y_SPEED, 0)
		if pressed_keys[K_d]:
			self.rect.move_ip(Player.Y_SPEED, 0)
		self.check_player_bounds()

	def check_player_bounds(self):
		"""Keep the player on the screen."""
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > config.SCREEN_WIDTH:
			self.rect.right = config.SCREEN_WIDTH
		if self.rect.top <= 0:
			self.rect.top = 0
		if self.rect.bottom >= config.SCREEN_HEIGHT:
			self.rect.bottom = config.SCREEN_HEIGHT
