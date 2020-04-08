# spaceship game

import os
import pygame
import random

from pygame.locals import (
	K_w,
	K_s,
	K_a,
	K_d,
	KEYDOWN,
	K_SPACE,
	QUIT
)

#constants for screen width and height
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700
_image_library = {}

# Player class that user controls
class Player(pygame.sprite.Sprite):
	def __init__(self):
		super(Player, self).__init__()
		#self.surf = pygame.Surface((30, 45))
		self.surf = get_image(os.path.join('assets', 'space_ship_v1.png'))
		#self.surf.fill((255, 255, 255))
		self.rect = self.surf.get_rect(
			center=(
				SCREEN_WIDTH / 2, SCREEN_HEIGHT
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
		if self.rect.right > SCREEN_WIDTH:
			self.rect.right = SCREEN_WIDTH
		if self.rect.top <= 0:
			self.rect.top = 0
		if self.rect.bottom >= SCREEN_HEIGHT:
			self.rect.bottom = SCREEN_HEIGHT

# Projectile class that destroys entities
class Projectile(pygame.sprite.Sprite):
	def __init__(self, center):
		super(Projectile, self).__init__()
		self.surf = pygame.Surface((5, 10))
		self.surf.fill((255, 0, 0))
		self.rect = self.surf.get_rect(center=center)
	
	def update(self):
		# update the projectile's location
		# remove the sprite when it passes the top edge of the screen
		self.rect.move_ip(0, -3)
		if self.rect.bottom < 0:
			self.kill()

# Enemy class that tries to destroy user
class Enemy(pygame.sprite.Sprite):
	def __init__(self):
		super(Enemy, self).__init__()
		self.surf = pygame.Surface((20, 10))
		self.surf.fill((255, 255, 255))
		self.rect = self.surf.get_rect(
			center=(
				random.randint(0, SCREEN_WIDTH),
				-random.randint(20, 100)
			)
		)
		self.speed = random.randint(5, 8)

	# move the sprite based on speed
	# remove the sprite when it passes the bottom edge of the screen
	def update(self):
		self.rect.move_ip(0, self.speed)
		if self.rect.top > SCREEN_HEIGHT:
			self.kill()

def get_image(path):
	"""Returns an image and initializes it if necessary"""
	global _image_library
	if path not in _image_library:
		image = pygame.image.load(path)
		_image_library[path] = image
	else:
		image = _image_library[path]
	return image

def add_to_sprite_groups(sprite, *groups):
	"""Add the sprite to all of the groups provided."""
	for group in groups:
		group.add(sprite)


# main game loop
def main():
	pygame.init()
	pygame.display.set_caption("Space Runner")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	# Custom event for adding new enemy
	ADDENEMY = pygame.USEREVENT + 1
	pygame.time.set_timer(ADDENEMY, 250)

	player = Player()

	# Create group to hold enemies for collision detection and position updates
	enemies = pygame.sprite.Group()
	# Create group to hold bullets for collision detection and position updates
	projectiles = pygame.sprite.Group()
	# Create group to hold all sprites for rendering
	all_sprites = pygame.sprite.Group()
	all_sprites.add(player)
	# game constants
	DELAY_TIME = 10
	# game variables
	score = 0
	running = True
	while running:
		pygame.time.delay(DELAY_TIME)

		# handle events
		for event in pygame.event.get():
			if event.type == QUIT:
				running = False
			elif event.type == ADDENEMY:
				# Create new enemy and add it to the appropriate groupds
				new_enemy = Enemy()
				add_to_sprite_groups(new_enemy, enemies, all_sprites)
			elif event.type == KEYDOWN and event.key == K_SPACE:
				# Fire a projectile
				# set the center to the players location
				new_projectile = Projectile(
					center=(
						player.rect.x + (player.surf.get_width() / 2),
						player.rect.y
					)
				)
				# add project to the lists
				add_to_sprite_groups(new_projectile, projectiles, all_sprites)


		pressed_keys = pygame.key.get_pressed()
		# update player
		player.update(pressed_keys)
		# update enemies position
		enemies.update()
		projectiles.update()
		screen.fill((0, 0, 0))
		# draw sprites on screen
		for entity in all_sprites:
			screen.blit(entity.surf, entity.rect)

		# check if any enemies have collided w the player
		if pygame.sprite.spritecollideany(player, enemies):
			player.kill()
			running = False
		# check if any enemies have collided w our player's projectiles
		pygame.sprite.groupcollide(projectiles, enemies, True, True)


		# update the display
		pygame.display.flip()

if __name__ == '__main__':
	main()