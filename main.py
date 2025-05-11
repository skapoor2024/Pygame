import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
   
    framerate = 60
    bg_color = "black"
    pygame.init()
    clk = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # adding both groups to Player container before intialization
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,updatable,drawable)

    player = Player(x = SCREEN_WIDTH/2,y= SCREEN_HEIGHT/2)    
    af = AsteroidField()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        for item in asteroids:
            if item.detect_collision(player):
                print("Game Over!")
                exit()
            
            for bullet in shots:

                if item.detect_collision(bullet):

                    bullet.kill()
                    item.split()
                    break
                    
        screen.fill(bg_color)
        
        # drawing the objects
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        dt = clk.tick(framerate)/1000

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}") 
    print(f"Screen height: {SCREEN_HEIGHT}") 

if __name__ == "__main__":
    main()
