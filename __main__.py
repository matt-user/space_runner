# spaceship game

import os

import pygame
import config

from projectile import Projectile
from model import Model
from level_handler import Level_Handler

from pygame.locals import (
	KEYDOWN,
	K_SPACE,
	QUIT
)

# main game loop
def main():
	os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (config.X_WIN_POS, config.Y_WIN_POS)
	pygame.init()
	pygame.display.set_caption("Space Runner")
	screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
	# Custom Events!
	# First level event
	FIRSTLEVEL = pygame.USEREVENT + 1
	# Add the first level event to the event queue
	pygame.time.set_timer(FIRSTLEVEL, 1000)
	level_handler = Level_Handler()
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
			elif event.type == FIRSTLEVEL:
				# Create the enemies for the first level!
				level_handler.load_level(1)
				# don't load another first level
				pygame.time.set_timer(FIRSTLEVEL, 0)
			elif event.type == KEYDOWN and event.key == K_SPACE:
				# Fire a projectile
				# set the center to the players location
				new_projectile = Projectile(center=(Model.get_instance().get_player_gun()))
				Model.get_instance().add_projectile(new_projectile)
		pressed_keys = pygame.key.get_pressed()
		# update the Model
		Model.get_instance().update(pressed_keys)
		screen.fill((0, 0, 0))
		# draw sprites on screen 
		# i dont like how all sprites is public
		# TODO: Implement a view class?
		for entity in Model.get_instance().all_sprites:
			screen.blit(entity.surf, entity.rect)
		if Model.get_instance().check_player_enemy_collision():
			running = False
		# check if any enemies have collided w our player's projectiles
		Model.get_instance().check_projectile_enemy_collision()
		# update the display
		pygame.display.flip()

if __name__ == '__main__':
	main()