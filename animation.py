"""The animation class is responsible for updating a sprites image."""

import os
import pygame

from utility import get_image

class Animation():
    def __init__(self, animation_delay, *file_path):
        """Construct  the animation."""
        image_folder_path = os.path.join(*file_path)
        image_files = [os.path.join(image_folder_path, f) for f in os.listdir(image_folder_path)]
        self.images = [get_image(f) for f in image_files]
        self.image_index = 0
        self.image_timer = 0
        self.animation_delay = animation_delay
    

    def get_image(self):
        """Returns the current animation image."""
        return self.images[self.image_index]

    def next_animation(self):
        """Returns the next animation image."""
        self.image_timer += 1
        if self.image_timer == self.animation_delay:
            self.image_index += 1
            self.image_timer = 0
        if self.image_index == len(self.images):
            self.image_index = 0
        return self.images[self.image_index]