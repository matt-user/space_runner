import pygame

from level_handler import Level_Handler
from model import Model
from projectile import Projectile

from pygame.locals import (
	KEYDOWN,
	K_SPACE,
	QUIT
)

class Controller():
	"""Class for managing the event loop and game."""

	def __init__(self):
		"""Initialze the display and prepare game objects."""
		self.screen = pygame.display.get_surface()
		self.clock = pygame.time.Clock()
		self.fps = 60.0
		self.pressed_keys = pygame.key.get_pressed()
		self.running = True
		self.level_handler = Level_Handler()
		# First level event
		self.FIRSTLEVEL = pygame.USEREVENT + 1
		pygame.time.set_timer(self.FIRSTLEVEL, 3000)

	def run(self):
		"""Main game loop."""
		while self.running:
			self.check_events()
			self.update()
			self.draw()
			self.check_collisions()
			# update the display
			pygame.display.flip()
			self.clock.tick(self.fps)

	def check_events(self):
		"""Check the game events."""
		for event in pygame.event.get():
			if event.type == QUIT:
				self.running = False
			elif event.type == self.FIRSTLEVEL:
				# Create the enemies for the first level!
				self.level_handler.load_level(1)
				# don't load another first level
				pygame.time.set_timer(self.FIRSTLEVEL, 0)
			elif event.type == KEYDOWN and event.key == K_SPACE:
				# Fire a projectile
				# set the center to the players location
				new_projectile = Projectile(center=(Model.get_instance().get_player_gun()))
				Model.get_instance().add_player_projectile(new_projectile)
	
	def update(self):
		"""Update the game objects."""
		self.pressed_keys = pygame.key.get_pressed()
		Model.get_instance().update(self.pressed_keys)
	
	def draw(self):
		"""Draw the game objects."""
		self.screen.fill((0, 0, 0))		
		# draw sprites on screen 
		# i dont like how all sprites is public
		# TODO: Implement a view class?
		for entity in Model.get_instance().all_sprites:
			self.screen.blit(entity.surf, entity.rect)
	
	def check_collisions(self):
		"""Check the game objects for collisions"""
		if Model.get_instance().check_player_enemy_collision():
			self.running = False
		# check if any enemies have collided w our player's projectiles
		Model.get_instance().check_projectile_enemy_collision()