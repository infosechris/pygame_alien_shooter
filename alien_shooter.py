import pygame

bg_color = (240, 245, 242)
txt_color = (0, 0, 0)
sc_width = 480
sc_height = 640	

pygame.init()
gamepad = pygame.display.set_mode((sc_width, sc_height))
pygame.display.set_caption('Alien Shooter')