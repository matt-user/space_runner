# spaceship game

import os

import pygame
import config

from controller import Controller

if __name__ == '__main__':
	os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (config.X_WIN_POS, config.Y_WIN_POS)
	pygame.init()
	pygame.display.set_caption("Space Runner")
	pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
	space_runner = Controller()
	space_runner.run()
	pygame.quit()
