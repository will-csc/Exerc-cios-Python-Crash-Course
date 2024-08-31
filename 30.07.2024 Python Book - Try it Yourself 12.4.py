import pygame
import sys

# Inicialize o Pygame
pygame.init()

class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print(f"The key pressed was {event.key}")

ai_settings = Settings()
screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
pygame.display.set_caption("12-4 Keys")

while True:
    check_events()
    screen.fill(ai_settings.bg_color)
    pygame.display.flip()
