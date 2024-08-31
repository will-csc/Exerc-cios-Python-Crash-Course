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

class Rocket():
	
	def __init__(self, screen):
		"""Initialize the ship and set its starting position."""
		self.screen = screen
		# Load the ship image and get its rect.
		self.image = pygame.image.load('rocket.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		# Start each new ship at the bottom center of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)
	
	def check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
				
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					self.rect.centerx += 5
				elif event.key == pygame.K_LEFT:
					self.rect.centerx -= 5
				elif event.key == pygame.K_DOWN:
					self.rect.bottom += 5
				elif event.key == pygame.K_UP:
					self.rect.bottom -= 5
		
def update_screen(ai_settings, screen, charac):
	"""Update images on the screen and flip to the new screen."""
	# Redraw the screen during each pass through the loop.
	screen.fill(ai_settings.bg_color)
	charac.blitme()
	# Make the most recently drawn screen visible.
	pygame.display.flip()

				
# Initialize game and create a screen object.
pygame.init()
ai_settings = Settings()
screen = pygame.display.set_mode(
			(ai_settings.screen_width, ai_settings.screen_height))
pygame.display.set_caption("Move Rocket")
# Make a rocket.
Rocket = Rocket(screen)
# Set the background color.
bg_color = (230, 230, 230)
# Start the main loop for the game.
while True:
	Rocket.check_events()
	update_screen(ai_settings, screen, Rocket)
	# Watch for keyboard and mouse events.
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit
	# Redraw the screen during each pass through the loop.
	screen.fill(ai_settings.bg_color)
	Rocket.blitme()
	# Make the most recently drawn screen visible.
	pygame.display.flip()
