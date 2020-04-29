import os
import operator
import pygame

import config
from utility import get_image
from animation import Animation
from model import Model
from projectile import Projectile
from utility import get_direction
from moving_object import Moving_Object

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
    FIRE_DELAY = 20
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
        self.fire_counter = 0
        self.can_fire = True
        self.moving_object = Moving_Object(Player.X_SPEED, self.rect)


    def update(self, pressed_keys):
        """Updates all of the player's information"""
        self.surf = self.animation.next_animation()
        self.update_firing()
        self.update_mouse_movement()
        if self.moving_object.is_moving:
            self.moving_object.update_location()
        #self.update_key_movement(pressed_keys)

    def update_mouse_movement(self):
        """Updates the player's position based on the mouse position"""
        mouse_pos = pygame.mouse.get_pos()
        self.moving_object.start_moving(mouse_pos)

    
    def update_firing(self):
        """Updates the player's firing status"""
        if self.fire_counter == Player.FIRE_DELAY:
            self.fire_counter = 0
            self.can_fire = True
        elif not self.can_fire:
            self.fire_counter += 1

    def fire(self):
        """Fire a projectile from the users gun"""
        # Fire a projectile if we can
        # set the center to the players location
        if self.can_fire:
            self.can_fire = False
            new_projectile = Projectile(center=self.get_gun())
            Model.get_instance().add_player_projectile(new_projectile)
    
    def get_gun(self):
        """Returns the players gun position."""
        return (
            self.rect.x + (self.surf.get_width() / 2),
            self.rect.y
        )

    def update_key_movement(self, pressed_keys):
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
    

