import pygame


class Ship():

    def __init__(self, ai_settings,screen):
        """Place ship on screen"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Loading the ship and creating ship rectangle
        self.image = pygame.image.load('images\plane.png')
        self.rect = self.image.get_rect()
        self.screen_rectangle = screen.get_rect()

        # Starting position for the ship
        self.rect.centerx = self.screen_rectangle.centerx
        self.rect.bottom = self.screen_rectangle.bottom

        # store movement as a float
        self.center = float(self.rect.centerx)

        # Movement Flg
        self.mv_right = False
        self.mv_left = False

    def update(self):
        """Update the position of the ship"""
        if self.mv_right and self.rect.right < self.screen_rectangle.right:
            self.center += self.ai_settings.ship_speed_settings
        if self.mv_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_settings

        self.rect.centerx = self.center

    def place_ship(self):
        """Drawing the ship to the current location"""
        self.screen.blit(self.image, self.rect)