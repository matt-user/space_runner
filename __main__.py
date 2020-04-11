# spaceship game

import os
import pygame
import random
import config

from player import Player
from projectile import Projectile
from enemy import Enemy

from pygame.locals import (
	KEYDOWN,
	K_SPACE,
	QUIT
)

def add_to_sprite_groups(sprite, *groups):
	"""Add the sprite to all of the groups provided."""
	for group in groups:
		group.add(sprite)


# main game loop
def main():
	pygame.init()
	pygame.display.set_caption("Space Runner")
	screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

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