import pygame
from pygame.sprite import Sprite
import random

class Alien(Sprite):
	"""A class to represent a single alien in the fleet."""
	def __init__(self, ai_settings, screen):
		"""Initialize the alien and set its starting position."""
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		# Load the alien image and set its rect attribute.
		aliens_imgs = ["alien1","alien2","alien3"]
		img = random.choice(aliens_imgs)
		self.image = pygame.image.load('images/' + img + '.bmp')
		self.rect = self.image.get_rect()
		# Start each new alien near the top left of the screen.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		# Store the alien's exact position.
		self.x = float(self.rect.x)
	def blitme(self):
		"""Draw the alien at its current location."""
		self.screen.blit(self.image, self.rect)
