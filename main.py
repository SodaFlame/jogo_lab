import pygame, sys
import spriteclass
from config import *
from TiledMapClass import TiledMap
from pytmx.util_pygame import load_pygame
from pygame.locals import *
from sprites import *

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
handled = False
    
#there was a clusterfuck of code in here but I've managed to clear it up with functions. If only I could do the same with these classes
       
class Knight(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, movement, is_clicked):
        super().__init__()
        self.walk_sprites = []
        self.x = pos_x
        self.y = pos_y
        self.xspeed = 2
        self.yspeed = 2
        self.is_vertical = True
        self.select_char = 0
        self.target_set = 0
        self.click = 0
        self.movement = 2400
        self.target_dest = [self.x, self.y]
        for x in range(0, len(todas_sprites_knight)):
            self.walk_sprites.append(todas_sprites_knight[x])
        self.current_sprite = 0    
        self.image = self.walk_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [self.x, self.y]
        
    
    def update(self):
        mouse = pygame.mouse.get_pressed()
        if mouse[0] and pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            pos = pygame.mouse.get_pos()
            self.select_char = 1
            self.click = 1
        if self.select_char == 1 and mouse[2]:
            pos = pygame.mouse.get_pos()
            self.target_dest = pos
            self.target_set = 1

        if idle:
            self.current_sprite += 0.06
            self.image = self.walk_sprites[int(self.current_sprite)]
            if self.current_sprite >= (8 - 0.03):
                self.current_sprite = 0
        
        if self.select_char == 1 and self.target_set ==  1 and self.click == 1:
            for tile_object in tmx_map.tmxdata.objects:
                if tile_object.name == 'wall':
                    wall = pygame.Rect(tile_object.x, tile_object.y, tile_object.width, tile_object.height)
                    if self.rect.colliderect(wall) and self.is_vertical == True:
                        self.yspeed = 0
                    elif self.rect.colliderect(wall):
                        self.xspeed = 0
                    
            if self.target_dest[1] > self.y:
                self.movement -= 40
                self.current_sprite += 0.05
                self.y += self.yspeed
                self.movement -= 1
                self.image = self.walk_sprites[int(self.current_sprite)+9]
                self.rect.center = [self.x, self.y]
                if self.current_sprite >= 17:
                    self.current_sprite = 9
                    
            elif self.target_dest[0] > self.x:
                self.movement -= 40
                self.current_sprite += 0.05
                self.x += self.xspeed
                self.movement -= 1
                self.image = self.walk_sprites[int(self.current_sprite)+17]
                self.rect.center = [self.x, self.y]
                if self.current_sprite >= 26:
                    self.current_sprite = 17
                self.is_vertical = False
            
            elif self.target_dest[0] < self.x:
                self.movement -= 40
                self.current_sprite += 0.05
                self.x -= self.xspeed
                self.image = self.walk_sprites[int(self.current_sprite)+26]
                self.rect.center = [self.x, self.y]
                if self.current_sprite >= 35:
                    self.current_sprite = 26
                self.is_vertical = False
            
            elif self.target_dest[1] < self.y:
                self.movement -= 40
                self.current_sprite += 0.05
                self.y -self.yspeed
                self.image = self.walk_sprites[int(self.current_sprite)+35]
                self.rect.center = [self.x, self.y]
                if self.current_sprite >= 44:
                    self.current_sprite = 35
            
        if self.movement <= 0:
            self.select_char = 0
            self.target_set = 0
            self.movement = 2400
            self.click = 0
                    
    def is_clicked(self):
        return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())
                    
                    
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
        
    for event in pygame.event.get(): # loop de comandos
        if event.type == QUIT: # pediu pra sair?
             pygame.quit() # sair do jogo
             sys.exit() # parar o programa
        if event.type == KEYDOWN: #se a tecla for pressionada
            if event.key == K_RIGHT: 
                right = True
            if event.key == K_LEFT:
                left = True  
            if event.key == K_UP:
                up = True
            if event.key == K_DOWN:
                down = True
        if event.type == KEYUP: #se a tecla for solta
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
    
    #will cause a blackscreen if removed
    surf = pygame.transform.scale(display, WINDOW_SIZE)
    screen.blit(surf, (0, 0))
    
    
    pygame.display.update() #updates the display
    fps.tick(60) # fps
