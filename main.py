import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys
from logger import log_state, log_event

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Player.containers = (updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable,)
  Shot.containers = (shots, updatable, drawable)

  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  asteroid_field = AsteroidField()

  dt = 0
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  while True:
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        log_event("KEYDOWN", key=pygame.key.name(event.key))
      elif event.type == pygame.QUIT:
        log_event("QUIT")
        return

    updatable.update(dt)

    for asteroid in asteroids:
      if asteroid.collision(player):
        print("Game over!")
        sys.exit()

    for asteroid in asteroids:
      for shot in shots:
        if shot.collision(asteroid):
          shot.kill()
          asteroid.split()

    pygame.Surface.fill(screen, "black")

    for item in drawable:
      item.draw(screen)

    pygame.display.flip()

    dt = clock.tick(60) / 1000
    log_state()


if __name__ == "__main__":
  main()