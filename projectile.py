import pygame

# Projectile class that destroys entities
class Projectile(pygame.sprite.Sprite):
	def __init__(self, center):
		super(Projectile, self).__init__()
		self.surf = pygame.Surface((5, 10))
		self.surf.fill((255, 0, 0))
		self.rect = self.surf.get_rect(center=center)
	
	def update(self):
		# update the projectile's location
		# remove the sprite when it passes the top edge of the screen
		self.rect.move_ip(0, -3)
		if self.rect.bottom < 0:
			self.kill()