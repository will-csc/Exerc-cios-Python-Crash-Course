import sys
import pygame

def run_game():
	pygame.init()
	screen = pygame.display.set_mode((1200,800))
	bg_color = (3, 11, 252)
	pygame.display.set_caption("Background Color")
	while True:
		screen.fill(bg_color)
		pygame.display.flip()

run_game()
