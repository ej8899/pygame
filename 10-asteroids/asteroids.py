import pygame, sys

pygame.init()

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
GAME_TITLE = "Asteroid Shooter"

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display_surface.fill(pygame.Color('grey46'))
# display_surface.fill((255,0,255)) # as RGB

pygame.display.set_caption(GAME_TITLE)

test_surface = pygame.Surface((400,100)) # x & y coords
test_surface.fill(pygame.Color('lightskyblue4'))

# start our game loop
while True:
    # check for input events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit();

    # update game parts

    # place graphics
    display_surface.blit(test_surface,(WINDOW_WIDTH-400,150))

    # show display surface
    pygame.display.update()