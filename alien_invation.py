import sys

import pygame

from settings import Settings

from ship import Ship

from bullet import Bullet

from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behaviour"""
    def __init__(self):
        """Initializ the game, and creating  Resorces"""
        pygame.init()
        self.clock = pygame.time.Clock()   
        self.settings = Settings() 
        #Group to store bullets in
        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()

        

        # setting up the screen
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height 
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)  # Creating an instance of Ship

        # seting Background colour

        self.bg_color = (0, 230, 230) # RGB color for light gray
        

    def run_game(self):
        """Strating the main loop for the game"""
        self._create_fleet()
        while True:

            self._check_events()
            self.ship.update()
            #self.bullets.update()
            
                        
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            self.clock.tick(60) # Limit the game to 60 frames per second

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                ##Moving the ship to the right when the right arrow key is pressed
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()  
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()      

    def _check_keyup_events(self,event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
             self.ship.moving_right = False           
        elif event.key == pygame.K_LEFT:
             self.ship.moving_left = False    

    def _fire_bullet(self):
        """Createing a new bullet and add it to the bullets group""" 
        if len(self.bullets) < self.settings.bullets_allowed:
           new_bullet = Bullet(self)
           self.bullets.add(new_bullet)               

    def _update_screen(self):
        """Update image on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)  # Fill the screen with the background color        
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self.bullets.update()
        #Deleting the bullets which have passed the screen
        for bullet in self.bullets.copy():
                if bullet.rect.bottom <=0:
                    self.bullets.remove(bullet)
        #print(len(self.bullets))      
            
        #print(self.bullets.sprites())
        #Check for bullets that have hit aliens and the giet rid of those
        self._check_bullet_alien_collisions()
        if not self.aliens:
            #Destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self):
        """Create the fleet of the aliens""" 
        #Making an alien
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size #size attribute of the rect object
        current_x,current_y = alien_width,alien_height

        while current_y < (self.settings.screen_height -3*alien_height):

            while current_x < (self.settings.screen_width -2*alien_width ):
                self._create_alien(current_x,current_y)
                current_x += alien_width *2

            current_x =alien_width
            current_y += alien_height*2       
    
    def _create_alien(self,x_position,y_position):
        """Create an alien and place it in the row"""
        new_alien =Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_aliens(self):
        """Update the position of all alens in fleet"""
        self._check_fleet_edges()
        self.aliens.update() 

        #Looking for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            print("Ship hit ,Pathetic Loser")   

    def _check_fleet_edges(self):
        """Respond if any alien have reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break    
    
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions using group-collisions of pugame
        which returns a dictionary conatining the bullets that have collided
          as keys and the aliens that have been hit as values"""
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)

if __name__ == '__main__':
    # Make a game instance, and Run the game
    ai = AlienInvasion()                       
    ai.run_game()
