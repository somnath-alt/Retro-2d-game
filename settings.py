class Settings:
    """A class to hold appliocation settings."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen Settings
        self.screen_width = 1523
        self.screen_height = 765
        self.bg_color = (230, 230, 230)
        self.ship_speed = 2.5
        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
        self.alien_speed = 1.5
        self.fleet_drop_speed = 15
        # fleet_direction of 1 represents right and -1 represents left
        self.fleet_direction =1
        self.ship_limit = 7
        