import pygame, sys
import spriteclass
from config import *
from TiledMapClass import TiledMap
from pytmx.util_pygame import load_pygame
from pygame.locals import *
from sprites import *
from classes import Knight
from classes import *

pygame.init()

#random shit that needs to be initialized here

fps = pygame.time.Clock()
pygame.display.set_caption("Jogo") #window name
WINDOW_SIZE = (1920, 1080)
display = pygame.Surface((1920, 1080))
screen = pygame.display.set_mode(WINDOW_SIZE,0,32) #creates the display
tmx_map = TiledMap('mapa3.tmx')
map_img = tmx_map.make_map()
map_rect = map_img.get_rect()

#booleans

right = False
left = False
up = False
down = False
idle = False
left_click = False
right_click = False
    
def draw_grid():
    for x in range(cols+1):
        pygame.draw.line(display, white, (x*tile_size, 0), (x*tile_size, WINDOW_SIZE[1]))
    for x in range(lines+1):
        pygame.draw.line(display, white, (0, x*tile_size), (WINDOW_SIZE[0], x*tile_size))
                                        

knight_sprite = pygame.sprite.Group()
k1 = Knight(945, 555, 6, 0)
k2 = Knight(400, 400, 6, 0)
knight_sprite.add(k1)
knight_sprite.add(k2)

while True: # game loop
    display.blit(map_img, (0,0))

    #handle key presses and etc
        
    for event in pygame.event.get(): #event loop
        if event.type == QUIT: # exit?
             pygame.quit() # exit the  game
             sys.exit() # stop the program
        if event.type == KEYDOWN: #if the key is pressed
            if event.key == K_RIGHT: 
                right = True
            if event.key == K_LEFT:
                left = True  
            if event.key == K_UP:
                up = True
            if event.key == K_DOWN:
                down = True
        if event.type == KEYUP: #if they key is released...
            if event.key == K_RIGHT:
                right = False
            if event.key == K_LEFT:
                left = False
            if event.key == K_UP:
                up = False
            if event.key == K_DOWN:
                down = False
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1: #1 = left, scroll 2, right 3, scroll up 4, scroll down 5
                left_click = True
            if event.button == 3:
                right_click = True
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                left_click = False
            if event.button == 3:
                right_click = False
        
    if right == False and left == False and up == False and down == False:
        idle = True
    
    
    draw_grid()
    knight_sprite.draw(display)
    knight_sprite.update()
   # gm.draw(display)
   # gm.update()
    
    #will cause a blackscreen if removed
    surf = pygame.transform.scale(display, WINDOW_SIZE)
    screen.blit(surf, (0, 0))
    
    
    pygame.display.update() #updates the display
    fps.tick(60) # fps
