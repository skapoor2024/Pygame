import pygame

# Base class for game objects

class CircleShape(pygame.sprite.Sprite):

    def __init__(self,x,y,radius):
        
        if hasattr(self,"containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius

    def draw(self,screen):
        # subclass must override
        pass
    
    def update(self,dt):
        #subclass must override
        pass

    def detect_collision(self,item):

        if isinstance(item,CircleShape):

            distance = self.position.distance_to(item.position)
            min_distance = self.radius + item.radius

            return distance<=min_distance
        
        else:

            raise Exception(f"Object is not of type circle change it")
