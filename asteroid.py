from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):

    def __init__(self,x,y,radius):

        self.x = x
        self.y = y
        
        super().__init__(x,y,radius)

    def draw(self,screen):

        pygame.draw.circle(screen,color = "white",center=self.position,radius=self.radius,width=2)
                
    def update(self,dt):

        self.position += self.velocity * dt

    def spawn_after_split(self,rand_angle):
        
        new_velocity = self.velocity.rotate(rand_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x,self.position.y,new_radius)
        asteroid.velocity = 1.2 * new_velocity

    def split(self):

        self.kill()
        
        if self.radius<= ASTEROID_MIN_RADIUS:

            return
        
        else:

            rand_angle = random.uniform(20,50)
            self.spawn_after_split(rand_angle)
            self.spawn_after_split(-rand_angle)



