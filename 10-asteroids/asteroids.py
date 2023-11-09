import pygame, sys

# GAME INI
pygame.init()

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
GAME_FRAMERATE = 120
GAME_TITLE = "Asteroid Shooter"


# important references:
# color list: https://www.pygame.org/docs/ref/color_list.html



display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display_surface.fill(pygame.Color('grey46'))
# display_surface.fill((255,0,255)) # as RGB

clock = pygame.time.Clock(); # use for frame rate limiter

pygame.display.set_caption(GAME_TITLE)

# helper functions
def writeCentered(text, x, y, color="Coral",):
    text = font.render(text, True, pygame.Color(color))
    text_rect = text.get_rect(center=(WINDOW_WIDTH//2, y))
    return text, text_rect



# IMAGE IMPORTS
ship_surf = pygame.image.load('./graphics/ship.png').convert_alpha(); # for alpha transparencies - or just .convert() if not.
ship_rect = ship_surf.get_rect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
ship_x_pos = 300;
ship_y_pos = 500;

background_surf = pygame.image.load('./graphics/background.png').convert();

laser_surf = pygame.image.load('./graphics/laser.png').convert_alpha();
laser_rect = laser_surf.get_rect(midbottom = (ship_rect.midtop))

# FONT IMPORTS
font = pygame.font.Font('./graphics/subatomic.ttf', 50);
text_surf, text_rect = writeCentered(GAME_TITLE, 0, 680,'darkorange') # this will be centered anyhow, but at 10 height

# GAME LOOP
while True:
    # EVENT LOOP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit();
    
    # framerate limit
    clock.tick(GAME_FRAMERATE);

    # mouse input
    # print(pygame.mouse.get_pos()); #returns (x,y)
    ship_rect.center = pygame.mouse.get_pos();
    print(pygame.mouse.get_pressed()); #returns (left,middle,right)

    # UPDATES
    laser_rect.y -= 10

    # DRAWING
    display_surface.fill(pygame.Color('grey46'))
    display_surface.blit(background_surf,(0,0))
    display_surface.blit(ship_surf,ship_rect)
    display_surface.blit(text_surf,text_rect)
    display_surface.blit(laser_surf,laser_rect)


    # show display surface
    pygame.display.update()
# end game loop