import pygame
from constants import *

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  # This is an infinite loop ... on purpose!
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    pygame.Surface.fill(screen,"black")
    pygame.display.flip()


if __name__ == "__main__":
  main()