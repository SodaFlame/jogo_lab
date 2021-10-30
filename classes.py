import pygame
from config import *
from sprites import *
from pytmx.util_pygame import load_pygame
from TiledMapClass import TiledMap


display = pygame.Surface((1920, 1080))
screen = pygame.display.set_mode((1920, 1080),0,32)
idle = True
tmx_map = TiledMap('mapa3.tmx')
map_img = tmx_map.make_map()
map_rect = map_img.get_rect()


class Knight(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, movement, is_clicked, is_ally):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.x = pos_x
        self.y = pos_y
        self.has_turn = True
        self.select_char = 0
        self.target_set = 0
        self.click = 0
        self.movement = 2400
        #Knight.attack = 0
        self.target_dest = [self.x, self.y]
        for x in range(0, len(todas_sprites_knight)):
            self.sprites.append(todas_sprites_knight[x])
        self.current_sprite = 0    
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [self.x, self.y]
        
    
class Knight(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, movement, is_clicked):
        super().__init__()
        self.sprites = []
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
            self.sprites.append(todas_sprites_knight[x])
        self.current_sprite = 0    
        self.image = self.sprites[self.current_sprite]
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
            self.image = self.sprites[int(self.current_sprite)]
            if self.current_sprite >= (8- 0.03):
                self.current_sprite = 0
        
        if self.select_char == 1 and self.target_set ==  1 and self.click == 1:
            
            if self.target_dest[1] > self.y:
                self.movement -= 40
                self.current_sprite += 0.05
                self.y += 2
                self.image = self.sprites[int(self.current_sprite)+9]
                self.rect.center = [self.x, self.y]
                if self.current_sprite >= 17:
                    self.current_sprite = 9
                    
            elif self.target_dest[0] > self.x:
                self.movement -= 40
                self.current_sprite += 0.05
                self.x += 2
                self.image = self.sprites[int(self.current_sprite)+17]
                self.rect.center = [self.x, self.y]
                if self.current_sprite >= 26:
                    self.current_sprite = 17
            
            elif self.target_dest[1] < self.y:
                self.movement -= 40
                self.current_sprite += 0.05
                self.y -= 2
                self.image = self.sprites[int(self.current_sprite)+35]
                self.rect.center = [self.x, self.y]
                if self.current_sprite >= 44:
                    self.current_sprite = 35
            
            elif self.target_dest[0] < self.x:
                self.movement -= 40
                self.current_sprite += 0.05
                self.x -= 2
                self.image = self.sprites[int(self.current_sprite)+26]
                self.rect.center = [self.x, self.y]
                if self.current_sprite >= 35:
                    self.current_sprite = 26
            
            
            if self.movement <= 0 or self.target_dest == [self.x, self.y]:
                self.select_char = 0
                self.target_set = 0
                self.click = 0
                self.movement = 2400
                
    def is_clicked(self):
        return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())
                
#         if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()) and self.click == 0 and self.movement == 0:
#             self.click = 0
#             self.movement = 0
#             print(self.current_sprite)
#             self.current_sprite += 0.05
#             self.image = self.sprites[int(self.current_sprite)+41]
#             self.rect.center = [self.x, self.y]
#             if self.current_sprite >= 50:
#                 self.current_sprite = 44
            
            
# class IgMenu(pygame.sprite.Sprite): #in-game menu
#     def __init__(self, width, height, color):
#         pygame.sprite.Sprite.__init__(self)
#         self.width = width
#         self.height = height
#         self.color = color
#         self.x = width
#         self.y = height
#         self.image = (pygame.image.load('thanos2.jpeg'))
        #self.rect = self.image.get_rect()
        #self.rect.center = [self.x, self.y]
        #self.attack = Knight.attack
        #IgMenu.done = False
    
#     def update(self):
#         mouse = pygame.mouse.get_pressed()
#         if Knight.attack == 1:
#             self.x = 500
#             self.y = 500
#             self.rect.center = [500, 500]
#         
#         if mouse[0] and pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
#             print('chungus')
#             IgMenu.done = True

#m1 = IgMenu(30, 30, blue)
#gm.add(m1)

        

            
             
        