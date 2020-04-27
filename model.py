"""This file defines the model class.
The model is responsible for keeping track of all of the game's entities."""

import pygame

from player import Player

class Model():
    __instance = None
    @staticmethod
    def get_instance():
        """Returns instance of the model if it does not exist"""
        if Model.__instance == None:
            Model()
        return Model.__instance

    def __init__(self):
        """Initialize the model with the groups necessary."""
        if Model.__instance != None:
            raise Exception("Error: This class is a singleton.  Can not directly construct")
        Model.__instance = self
        # Create group to hold enemies for collision detection and position updates
        self.enemies = pygame.sprite.Group()
        # Create group to hold bullets for collision detection and position updates
        self.player_projectiles = pygame.sprite.Group()
        # Create group to hold bullets for the enemies
        self.enemy_projectiles = pygame.sprite.Group()
        # Create group to hold all sprites for rendering
        self.all_sprites = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
    
    def update(self, pressed_keys):
        """Update all of the groups in model."""
        self.player.update(pressed_keys)
        self.enemies.update()
        self.player_projectiles.update()
        self.enemy_projectiles.update()

    def check_projectile_enemy_collision(self):
        """Checks if a projectile has collided with an enemy
           and removes the enemy if so."""
        pygame.sprite.groupcollide(self.player_projectiles, self.enemies, True, True)

    def check_player_enemy_collision(self):
        """Returns true if the player has collided into an enemy and removes player from game."""
        player_collided = pygame.sprite.spritecollideany(self.player, self.enemies)
        if player_collided:
            self.player.kill()
        return player_collided

    def get_player_gun(self):
        """Returns the players gun position."""
        return (
            self.player.rect.x + (self.player.surf.get_width() / 2),
			self.player.rect.y
        )
    
    def get_player_center(self):
        """Returns the center of the player's position"""
        return (
            self.player.rect.x + (self.player.surf.get_width() / 2),
            self.player.rect.y + (self.player.surf.get_height() / 2)
        )

    def add_enemy(self, enemy):
        """Adds the enemy to the appropriate groups."""
        self.__add_to_sprite_groups(enemy, self.enemies, self.all_sprites)

    def add_player_projectile(self, projectile):
        """Adds the projectile to the appropriate groups."""
        self.__add_to_sprite_groups(projectile, self.player_projectiles, self.all_sprites)
    
    def add_enemy_projectile(self, projectile):
        """Add the projectile to the enemy projectile groups."""
        self.__add_to_sprite_groups(projectile, self.enemy_projectiles, self.all_sprites)

    def __add_to_sprite_groups(self, sprite, *groups):
        """Add the sprite to all of the groups provided."""
        for group in groups:
            group.add(sprite)
