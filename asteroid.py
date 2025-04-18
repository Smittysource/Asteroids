from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        neg_angle = 0 - angle

        
        original_angle = self.velocity.as_polar()[1]
        new_less_velocity = pygame.Vector2.from_polar((1,original_angle))
        new_less_velocity.rotate_ip(angle)
        length = self.velocity.length()
        new_less_velocity *= length
        new_more_velocity = pygame.Vector2.from_polar((1,original_angle))
        new_more_velocity.rotate_ip(neg_angle)
        new_more_velocity *= length
        print(length)
        print(f"Original: {original_angle}\nAngle to turn: {angle}\nNew angle: {new_less_velocity.as_polar()[1]}")

        #print(f"{angle}  ----  {neg_angle}")
        #new_less_velocity = pygame.Vector2(0,1)
#        new_less_velocity = self.velocity#pygame.Vector2(0,1).rotate(self.velocity.as_polar()[0])
#        new_less_velocity.rotate_ip(45)
        #print(new_less_velocity)
#        new_greater_velocity = self.velocity
#        new_less_velocity.rotate_ip(0-45)
        #print(new_greater_velocity)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_less_velocity * 1.2
        asteroid2.velocity = new_more_velocity * 1.2
