"""Floater class that inherits from enemy"""

from enemy import Enemy
from animation import Animation

# Float enemy that inherits from enemy
# this enemy simply floats down the screen
class Floater(Enemy):
	ANIMATION_DELAY = 10
	FLOATER_SPEED = 2
	FIlE_PATH = ['assets', 'enemy', 'floater']

	def __init__(self, center):
		super().__init__(center, Floater.FLOATER_SPEED, Floater.ANIMATION_DELAY, *Floater.FIlE_PATH)
		self.speed = Floater.FLOATER_SPEED
	
	def update(self):
		"""Update the behavior of a Floater enemy."""
		Enemy.update(self)
		self.rect.move_ip(0, self.speed)