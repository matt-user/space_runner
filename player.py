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
	def __init__(self):
		super(Player, self).__init__()
		#self.surf = pygame.Surface((30, 45))
		self.surf = get_image(os.path.join('assets', 'space_ship_v1.png'))
		#self.surf.fill((255, 255, 255))
		self.rect = self.surf.get_rect(
			center=(
				config.SCREEN_WIDTH / 2, config.SCREEN_HEIGHT
			)
		)

	def update(self, pressed_keys):
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