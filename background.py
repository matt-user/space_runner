"""Class for maintaining the background image."""

import os
import pygame

from pygame.locals import (
    K_w,
    K_s,
    K_a,
    K_d
)

from utility import get_image

class Background():
    def __init__(self):
        self.color = pygame.Color("black")
    
    def set_tiles(self, screen):
        """Load the images for the background tiles."""
        # load the background tiles
        image_folder_path = os.path.join('assets', 'background')
        image_files = [os.path.join(image_folder_path, f) for f in os.listdir(image_folder_path)]
        image_files = [
                        [image_files[0], image_files[1]],
                        [image_files[2], image_files[3]]
                    ]
        self.tiles = [[get_image(f) for f in row] for row in image_files]
        self.stage_pos_x = 0
        self.stage_pos_y = 0
        self.tile_width = self.tiles[0][0].get_width()
        self.tile_height = self.tiles[0][0].get_height()
        screen.blit(self.tiles[0][0], [0, 0])
        self.surface = screen.copy()
    
    def update(self, pressed_keys, screen):
        """Updates the background based on the pressed keys."""
        if pressed_keys[K_d]:
            self.scroll(-5, 0, screen)
        if pressed_keys[K_a]:
            self.scroll(5, 0, screen)
        if pressed_keys[K_w]:
            self.scroll(0, 5, screen)
        if pressed_keys[K_s]:
            self.scroll(0, -5, screen)

    def scroll(self, x, y, screen):
        """Scroll the background."""
        self.stage_pos_x -= x
        self.stage_pos_y -= y
        col = (self.stage_pos_x % (self.tile_width * len(self.tiles[0]))) // self.tile_width
        x_off = (0 - self.stage_pos_x % self.tile_width)
        row = (self.stage_pos_y % (self.tile_height * len(self.tiles))) // self.tile_height
        y_off = (0 - self.stage_pos_y % self.tile_height)
        col2 = ((self.stage_pos_x + self.tile_width) % (self.tile_width * len(self.tiles[0]))) // self.tile_width
        row2 = ((self.stage_pos_y + self.tile_height) % (self.tile_height * len(self.tiles))) // self.tile_height
        screen.blit(self.tiles[row][col], [x_off, y_off])
        screen.blit(self.tiles[row][col2], [x_off + self.tile_width, y_off])
        screen.blit(self.tiles[row2][col], [x_off, y_off + self.tile_height])
        screen.blit(self.tiles[row2][col2], [x_off + self.tile_width, y_off + self.tile_height])
        self.surface = screen.copy()
