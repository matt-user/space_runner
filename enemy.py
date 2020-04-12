import pygame
import random
import config

# Enemy class that tries to destroy user
class Enemy(pygame.sprite.Sprite):
	def __init__(self):
		super(Enemy, self).__init__()
		self.surf = pygame.Surface((20, 10))
		self.surf.fill((255, 255, 255))
		self.rect = self.surf.get_rect(
			center=(
				random.randint(0, config.SCREEN_WIDTH),
				-random.randint(20, 100)
			)
		)
		self.speed = random.randint(5, 8)

	# move the sprite based on speed
	# remove the sprite when it passes the bottom edge of the screen
	def update(self):
		self.rect.move_ip(0, self.speed)
		if self.rect.top > config.SCREEN_HEIGHT:
			self.kill()