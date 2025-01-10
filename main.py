import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot

def main():
   print("Starting asteroids!")
   print(f"Screen width: {SCREEN_WIDTH}")
   print(f"Screen height: {SCREEN_HEIGHT}")


   pygame.init()
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   clock = pygame.time.Clock()
   dt = 0

   updatable = pygame.sprite.Group()
   drawable = pygame.sprite.Group()
   asteroids = pygame.sprite.Group()
   shots = pygame.sprite.Group()

   Player.containers = (updatable, drawable)
   player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

   Asteroid.containers = (asteroids, updatable, drawable)

   AsteroidField.containers = (updatable)
   asteroidField = AsteroidField()

   Shot.containers = (shots, updatable, drawable)

   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            return
         
      for obj in updatable:
         obj.update(dt)

      for asteroid in asteroids:
         if asteroid.checkCollision(player):
            print("Game over!")
            exit(1)
         for shot in shots:
            if shot.checkCollision(asteroid):
               shot.kill()
               asteroid.split()
         
      screen.fill("black")
      
      for obj in drawable:
         obj.draw(screen)

      pygame.display.flip()

      # limit framerate to 60fps
      dt = clock.tick(60) / 1000

if __name__ == "__main__":
   main()