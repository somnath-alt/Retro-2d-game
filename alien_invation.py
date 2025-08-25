import sys

import pygame

from settings import Settings

from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behaviour"""
    def __init__(self):
        """Initialize the game, and create the Resorces"""
        pygame.init()
        self.clock = pygame.time.Clock()  # Creating a clock object 
        self.settings = Settings()  # Creating an instance of Settings
        
        # setting up the screen
        self.screen = pygame.display.set_mode((self.settings.screen_widyh, self.settings.screen_height)) 
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)  # Creating an instance of Ship

        # seting Background colour

        self.bg_color = (230, 230, 230) # RGB color for light gray


    def run_game(self):
        """Strating the main loop for the game"""
        while True:
            # Watch for keyboard and Mouse Events 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)  # Fill the screen with the background color        
            
            self.ship.blitme()
            # Make the most recently drawn screen Visible
            pygame.display.flip()
            self.clock.tick(60) # Limit the game to 60 frames per second

if __name__ == '__main__':
    # Make a game instance, and Run the game
    ai = AlienInvasion()                       
    ai.run_game()