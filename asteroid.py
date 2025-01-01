import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    containers = ()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.position), self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
           return
        else:
           random_angle = random.uniform(20, 50)
           angle_1 = self.velocity.rotate(random_angle)
           angle_2 = self.velocity.rotate(-random_angle)

           old_radius = self.radius
           new_radius = old_radius - ASTEROID_MIN_RADIUS

           asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
           asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

           asteroid_1.velocity = angle_1 * 1.2
           asteroid_2.velocity = angle_2 * 1.2
