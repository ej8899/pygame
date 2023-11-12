import pygame, sys

# important references:
# color list: https://www.pygame.org/docs/ref/color_list.html


# GAME INI
# we could init everything, but it takes time to run:
# pygame.init() 
# only init what we're using for performance purposes:
pygame.font.init()

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
GAME_FRAMERATE = 120
GAME_TITLE = "Asteroid Shooter"

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

# update lasers
def laser_update(laser_list, speed = 300):
    for rect in laser_list:
        rect.y -= speed * DELTA_TIME
        if(rect.bottom < 0):
            laser_list.remove(rect)


# IMAGE IMPORTS
ship_surf = pygame.image.load('./graphics/ship.png').convert_alpha(); # for alpha transparencies - or just .convert() if not.
ship_rect = ship_surf.get_rect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
ship_x_pos = 300;
ship_y_pos = 500;

background_surf = pygame.image.load('./graphics/background.png').convert();

laser_surf = pygame.image.load('./graphics/laser.png').convert_alpha();
laser_list = []
# laser_rect = laser_surf.get_rect(midbottom = (ship_rect.midtop))

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            laser_rect = laser_surf.get_rect(midbottom = ship_rect.midtop)
            laser_list.append(laser_rect)
            # print(laser_list)
    
    # framerate limit
    DELTA_TIME = clock.tick(GAME_FRAMERATE) / 1000;
  

  
    # UPDATES
    laser_update(laser_list)
    ship_rect.center = pygame.mouse.get_pos();
    
    # DRAWING
    display_surface.fill(pygame.Color('grey46'))
    display_surface.blit(background_surf,(0,0))
    display_surface.blit(ship_surf,ship_rect)
    display_surface.blit(text_surf,text_rect)

    # draw the lasers
    for rect in laser_list:
        display_surface.blit(laser_surf,rect)

    # show display surface
    pygame.display.update()
# end game loop