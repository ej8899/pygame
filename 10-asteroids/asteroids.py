import pygame, sys

pygame.init()

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
GAME_TITLE = "Asteroid Shooter"

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display_surface.fill(pygame.Color('grey46'))
# display_surface.fill((255,0,255)) # as RGB


pygame.display.set_caption(GAME_TITLE)

# helper functions
def writeCentered(text, x, y, color="Coral",):
    text = font.render(text, True, pygame.Color(color))
    text_rect = text.get_rect(center=(WINDOW_WIDTH//2, y))
    return text, text_rect



# image imports
ship_surf = pygame.image.load('./graphics/ship.png').convert_alpha(); # for alpha transparencies - or just .convert() if not.
background_surf = pygame.image.load('./graphics/background.png').convert();

# font imports
font = pygame.font.Font('./graphics/subatomic.ttf', 50);
# text_surf = font.render(GAME_TITLE, True, pygame.Color('darkorange')); # text, antialiasing (true or false), color
# text_rect = text_surf.get_rect(center=(WINDOW_WIDTH/2,680))


text_surf, text_rect = writeCentered(GAME_TITLE, 0, 680,'darkorange') # this will be centered anyhow, but at 10 height

# start our game loop
while True:
    # check for input events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit();

    # update game parts

    # place graphics
    display_surface.fill(pygame.Color('grey46'))
    display_surface.blit(background_surf,(0,0))
    display_surface.blit(ship_surf,(300,500))
    display_surface.blit(text_surf,text_rect)

    # show display surface
    pygame.display.update()