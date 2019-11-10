import pygame
from pygame.sprite import Sprite

class Round(Sprite):
    """Manages bullets fire from players ship"""

    def __init__(self, ai_settings, window, ship):
        """Create a bullet at the ships current position"""
        super(Round, self).__init__()
        self.window = window

        """Create a retange at o"""
        self.rect = pygame.Rect(0, 0, ai_settings.round_w,
                                ai_settings.round_h)
      
        self.rect.top = ship.rect.top

        # rounds position is stored at 0
        self.y = float(self.rect.y)

        self.color = ai_settings.round_clr
        self.speed = ai_settings.round_speed

    def update(self):
        """Move th round up"""
        # update the rounds position
        self.y -= self.speed
        # update rounds box position
        self.rect.y = self.y


    def print_round(self):
        """Summon the round to the screen"""
        pygame.draw.rect(self.window, self.color, self.rect)