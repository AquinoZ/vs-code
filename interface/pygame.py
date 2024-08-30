import pygame
pygame.init()
windows = pygame.display.set_mode([500, 500])

loop = True
while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False
        pygame.display.update()