import sys
import pygame
from ship import Ship
from pygame.sprite import Group
from settings import Settings
import game_functions as gf
from alien import Alien

def run_game():
	# Initialize game and create a screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
			(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	# Make a ship, a group of bullets, and a group of aliens.
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()
	# Create the fleet of aliens.
	gf.create_fleet(ai_settings, screen, aliens)
	# Set the background color.
	bg_color = (230, 230, 230)
	
	# Start the main loop for the game.
	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)
		# Redraw the screen during each pass through the loop.
		screen.fill(ai_settings.bg_color)
		ship.blitme()
		# Make the most recently drawn screen visible.
		pygame.display.flip()
		
run_game()
