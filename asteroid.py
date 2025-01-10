import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
   def __init__(self, x, y, radius):
      super().__init__(x, y, radius)

   def draw(self, screen):
      pygame.draw.circle(screen, "white", self.position, self.radius, 2)

   def update(self, dt):
      self.position += (self.velocity * dt)

   def split(self):
      self.kill()
      if self.radius <= ASTEROID_MIN_RADIUS:
         return
      else:
         newAngle = random.uniform(20, 50)
         vec1 = pygame.Vector2(self.velocity.rotate(newAngle))
         vec2 = pygame.Vector2(self.velocity.rotate(-newAngle))
         newRadius = self.radius - ASTEROID_MIN_RADIUS
         ast1 = Asteroid(self.position.x, self.position.y, newRadius)
         ast2 = Asteroid(self.position.x, self.position.y, newRadius)
         ast1.velocity = vec1 * 1.2
         ast2.velocity = vec2 * 1.2