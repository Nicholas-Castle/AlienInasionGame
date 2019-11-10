import pygame
from pygame.sprite import Group

from settings import Settings
from space_ship import Ship
import invaders_funct as gf


def start_window():
    # start the game and make a screen object and settings for the game
    pygame.init()
    ai_settings = Settings()
    window = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_hieght)
    )
    pygame.display.set_caption("Inavders Return!")

    # spawn ship
    ship = Ship(ai_settings, window)
    # Store rounds in a group
    rounds = Group()
    # Game Main loop
    while True:
        gf.check_events(ai_settings, window, ship, rounds)
        ship.update()
        rounds.update()
        gf.update_rounds(rounds)
        gf.update_window(ai_settings, window, ship, rounds)




start_window()
