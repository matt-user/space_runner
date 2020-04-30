import operator
import math
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

# TODO: make a geometry class for shit like this
def get_direction(point_a, point_b):
	"""Returns the normalized direction from point a to the point b."""
	x_dif, y_dif = map(operator.sub, point_b, point_a)
	magnitude = math.sqrt((x_dif ** 2) + (y_dif ** 2))
	# if the points are the same return a 0 vector
	if magnitude == 0:
		return 0, 0
	x_dif_normed = x_dif / magnitude
	y_dif_normed = y_dif / magnitude
	return x_dif_normed, y_dif_normed

def get_rotation_angle(x_dir, y_dir):
	"""Returns the rotation angle of the two directions."""
	# to avoid an infinite angle return 0
	if x_dir == 0:
		return 0
	rotation_angle = -math.atan2(y_dir, x_dir) * (180.0 / math.pi) - 90.0
	return rotation_angle