from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOT_SPEED, PLAYER_SHOOT_COOLDOWN 
import pygame
from shot import Shot

class Player(CircleShape):

    def __init__(self,x,y):

        self.x = x
        self.y = y
        self.rotation = 0
        super().__init__(self.x,self.y,PLAYER_RADIUS)
                
        self.timer = 0
    
    # in the player class
    def triangle(self):

        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # draw the player class
    def draw(self,screen):

        pygame.draw.polygon(screen,color = "white",points = self.triangle(),width = 2)

    # rotate player
    def rotate(self,dt):
        
        self.rotation += PLAYER_TURN_SPEED * dt
    
    # move player
    def move(self,dt):

        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    # update method
    def update(self,dt):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            
            return self.rotate(-dt)
                
        if keys[pygame.K_d]:

            return self.rotate(dt)
        if keys[pygame.K_w]:

            return self.move(dt)

        if keys[pygame.K_s]:

            return self.move(-dt)

        if keys[pygame.K_SPACE]:
            
            if self.timer <=0:
                self.shoot()
                self.timer = PLAYER_SHOOT_COOLDOWN
        
        if self.timer > 0:

            self.timer-=dt

    # to shoot method
    def shoot(self):


        shot = Shot(self.position.x ,self.position.y)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOT_SPEED





