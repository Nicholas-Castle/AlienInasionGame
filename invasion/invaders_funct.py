import sys

import pygame
from round import Round

def check_events(ai_settings, window, ship, rounds):
    """Making the ship respond to mouse and key presses"""
    for evnt in pygame.event.get():
        if evnt.type == pygame.QUIT:
            sys.exit()
        elif evnt.type == pygame.KEYDOWN:
            key_d(evnt, ai_settings, window, ship, rounds)
        elif evnt.type == pygame.KEYUP:
            key_u(evnt, ship)

def key_d(evnt, ai_settings, window, ship, rounds):
    """move when key is pressed"""
    if evnt.key == pygame.K_RIGHT:
        ship.mv_right = True
    elif evnt.key == pygame.K_LEFT:
        ship.mv_left = True
    elif evnt.key == pygame.K_SPACE:
        fire_round(ai_settings, window, ship, rounds)

def fire_round(ai_settings, window, ship, rounds):
    if len(rounds) < ai_settings.num_rounds_on_screen:
        new_round = Round(ai_settings, window, ship)
        rounds.add(new_round)

def key_u(evnt, ship):
    """move when key is pressed"""
    if evnt.key == pygame.K_RIGHT:
        ship.mv_right = False
    elif evnt.key == pygame.K_LEFT:
        ship.mv_left = False

def update_rounds(rounds):
    """update the position and delete the round"""
    # Delete rounds after the go out of the window
    for round in rounds.copy():
        if round.rect.bottom <= 0:
            rounds.remove(round)

def update_window(ai_settings, window, ship, round):
    """Update the images on screen and flip window"""

    # draw the screen through each loop pass
    window.fill(ai_settings.bg_color)
    ship.place_ship()

    # Redraw rounds top and bottom
    for rounds in round.sprites():
        rounds.print_round()
    # draw screen
    pygame.display.flip()