import sys
import pygame

class Settings():
	"""A class to store all settings for Alien Invasion."""
	def __init__(self):
		"""Initialize the game's settings."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

class Character():
	
	def __init__(self, screen):
		"""Initialize the ship and set its starting position."""
		self.screen = screen
		# Load the ship image and get its rect.
		self.image = pygame.image.load('gon.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		# Start each new ship at the bottom center of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)

def update_screen(ai_settings, screen, charac):
	"""Update images on the screen and flip to the new screen."""
	# Redraw the screen during each pass through the loop.
	screen.fill(ai_settings.bg_color)
	charac.blitme()
	# Make the most recently drawn screen visible.
	pygame.display.flip()
	
ai_settings = Settings()
screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
pygame.display.set_caption("12-2 Game Character")
Gon = Character(screen)

while True:
	update_screen(ai_settings, screen, Gon)
	# Redraw the screen during each pass through the loop.
	screen.fill(ai_settings.bg_color)
	Gon.blitme()
	# Make the most recently drawn screen visible.
	pygame.display.flip()
	
	
	
