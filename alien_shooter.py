import pygame

#Variables needed for Gamepad
bg_color = (240, 245, 242)
txt_color = (0, 0, 0)
sc_width = 480
sc_height = 640	

#Initialized Game, Gamepad size, BG color, Game Title 
pygame.init()
gamepad = pygame.display.set_mode((sc_width, sc_height))
gamepad.fill(bg_color)
pygame.display.set_caption('Alien Shooter')

#Makes the game screen stay on for now
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

global gamepad
global jet

def drawObject(obj,x,y):
	global gamepad
	gamepad.blit(obj,(x,y))

drawobject(jet,200,350)