class Settings():
    """Stores settings for invaders_remake"""

    def __init__(self):
        """init game settings"""
        # Set Screen
        self.screen_width = 1200
        self.screen_hieght = 800
        self.bg_color = (176, 223, 229)

        # Ship Settings
        self.ship_speed_settings = .7

        # Bullet Settings
        self.round_speed = 1
        self.round_w = 3
        self.round_h = 15
        self.round_clr = 50, 50, 50
        self.num_rounds_on_screen = 10