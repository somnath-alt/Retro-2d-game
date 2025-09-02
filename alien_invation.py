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
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) 
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)  # Creating an instance of Ship

        # seting Background colour

        self.bg_color = (230, 230, 230) # RGB color for light gray


    def run_game(self):
        """Strating the main loop for the game"""
        while True:

            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60) # Limit the game to 60 frames per second

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                ##Moving the ship to the right when the right arrow key is pressed
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False           
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False    

    def _update_screen(self):
        """Update image on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)  # Fill the screen with the background color        
        self.ship.blitme()
        pygame.display.flip()
            
            

if __name__ == '__main__':
    # Make a game instance, and Run the game
    ai = AlienInvasion()                       
    ai.run_game()