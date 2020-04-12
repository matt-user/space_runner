import os
import pygame
import config
from utility import get_image

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

	def __init__(self):
		super(Player, self).__init__()
		# load all of the players animations
		image_folder_path = os.path.join('assets', 'player')
		image_files = [os.path.join(image_folder_path, f) for f in os.listdir(image_folder_path)]
		self.images = [get_image(f) for f in image_files]
		self.image_index = 0
		self.image_timer = 0
		self.surf = self.images[self.image_index]
		self.rect = self.surf.get_rect(
			center=(
				config.SCREEN_WIDTH / 2, config.SCREEN_HEIGHT
			)
		)


	def update(self, pressed_keys):
		"""Updates all of the player's information"""
		self.update_animation()
		self.update_movement(pressed_keys)
		
	
	def update_animation(self):
		"""Update player animation."""
		self.image_timer += 1
		if self.image_timer == Player.ANIMATION_DELAY:
			self.image_index += 1
			self.image_timer = 0
		if self.image_index == len(self.images):
			self.image_index = 0
		self.surf = self.images[self.image_index]

	def update_movement(self, pressed_keys):
		"""Update player movement based on pressed keys"""
		# update the players movement based on the pressed keys
		if pressed_keys[K_w]:
			self.rect.move_ip(0, -5)
		if pressed_keys[K_s]:
			self.rect.move_ip(0, 5)
		if pressed_keys[K_a]:
			self.rect.move_ip(-5, 0)
		if pressed_keys[K_d]:
			self.rect.move_ip(5, 0)

		# keep the player on the screen
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > config.SCREEN_HEIGHT:
			self.rect.right = config.SCREEN_WIDTH
		if self.rect.top <= 0:
			self.rect.top = 0
		if self.rect.bottom >= config.SCREEN_HEIGHT:
			self.rect.bottom = config.SCREEN_HEIGHT
