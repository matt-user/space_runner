import pygame
import config

# Functions needed from multiple files

def get_image(path):
	"""Returns an image and initializes it if necessary"""
	if path not in config._image_library:
		image = pygame.image.load(path)
		config._image_library[path] = image
	else:
		image = config._image_library[path]
	return image