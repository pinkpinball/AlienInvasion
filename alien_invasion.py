
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship 
import game_functions as gf


def run_game():
    # Initilize pygame, settings, and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship.
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets.
    bullets = Group()

    #Start themain loop for the game.
    while True:
        # Watch for keyboard and mouse events

        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets) 
        gf.update_screen(ai_settings, screen, ship, bullets)



run_game()