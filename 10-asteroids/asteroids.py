import pygame, sys

pygame.init()

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# start our game loop
while True:
    # check for input events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit();

    # update game parts


    # place graphics
    

    # show display surface
    pygame.display.update()