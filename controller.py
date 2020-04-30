import pygame

import config

from model import Model
from enemy_factory import create_enemy

from pygame.locals import (
    KEYDOWN,
    K_SPACE,
    K_ESCAPE,
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
        # First level event
        self.FIRSTLEVEL = pygame.USEREVENT + 1
        pygame.time.set_timer(self.FIRSTLEVEL, 1000)

    def load_level(self, level):
        """Loads the game objects based on the given level."""
        self.level_one_enemy_info = [
            { "location": (10, -10), "enemy_type": "Floater", "waypoints": [], "firepoints": [] },
            { "location": (50, -50), "enemy_type": "Floater", "waypoints": [], "firepoints": [] },
            { "location": (config.SCREEN_WIDTH / 2, -900), "enemy_type": "Floater", "waypoints": [], "firepoints": [] },
            { "location": ((config.SCREEN_WIDTH / 2) - 30, -1000), "enemy_type": "Floater", "waypoints": [], "firepoints": [] },
            { "location": ((config.SCREEN_WIDTH / 2) + 50, -1100), "enemy_type": "Floater", "waypoints": [], "firepoints": [] },
            { "location": (config.SCREEN_WIDTH / 2, -1200), "enemy_type": "Mall_Fighter", "waypoints": [(300, 300), (800, 600)], "firepoints": [(300, 150), (300, 300)] }
        ]
        if level == 1:
            for enemy_info in self.level_one_enemy_info:
                new_enemy = create_enemy(
                    enemy_info["location"], enemy_info["enemy_type"],
                    enemy_info["waypoints"], enemy_info["firepoints"]
                )
                Model.get_instance().add_enemy(new_enemy)


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
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                self.running = False
            elif event.type == self.FIRSTLEVEL:
                # Create the enemies for the first level!
                # self.load_level(1)
                # don't load another first level
                pygame.time.set_timer(self.FIRSTLEVEL, 0)
            elif event.type == KEYDOWN and event.key == K_SPACE:
                player = Model.get_instance().get_player()
                player.fire()
    
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
        # check if the player has collided w the enemies' projectiles
        if Model.get_instance().check_projectile_player_collision():
            self.running = False
        # check if any enemies have collided w our player's projectiles
        Model.get_instance().check_projectile_enemy_collision()