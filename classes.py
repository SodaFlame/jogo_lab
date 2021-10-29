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
        self.attack = 0
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
            if self.current_sprite >= (8 - 0.03):
                self.current_sprite = 0
        
        if self.select_char == 1 and self.target_set ==  1 and self.click == 1 and self.attack == 0:
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
                self.image = self.sprites[int(self.current_sprite)+9]
                self.rect.center = [self.x, self.y]
                if self.current_sprite >= 17:
                    self.current_sprite = 9
                    
            elif self.target_dest[0] > self.x:
                self.movement -= 40
                self.current_sprite += 0.05
                self.x += self.xspeed
                self.movement -= 1
                self.image = self.sprites[int(self.current_sprite)+17]
                self.rect.center = [self.x, self.y]
                if self.current_sprite >= 26:
                    self.current_sprite = 17
                self.is_vertical = False
            
            elif self.target_dest[0] < self.x:
                self.movement -= 40
                self.current_sprite += 0.05
                self.x -= self.xspeed
                self.image = self.sprites[int(self.current_sprite)+26]
                self.rect.center = [self.x, self.y]
                if self.current_sprite >= 35:
                    self.current_sprite = 26
                self.is_vertical = False
            
            elif self.target_dest[1] < self.y:
                self.movement -= 40
                self.current_sprite += 0.05
                self.y -self.yspeed
                self.image = self.sprites[int(self.current_sprite)+35]
                self.rect.center = [self.x, self.y]
                if self.current_sprite >= 44:
                    self.current_sprite = 35
            
            if self.movement <= 0:
                self.select_char = 0
                self.target_set = 0
                self.movement = 0
                self.click = 0
            
            
#         if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()) and self.click == 0 and self.movement == 0:
#             self.click = 0
#             self.movement = 0
#             print(self.current_sprite)
#             self.current_sprite += 0.05
#             self.image = self.sprites[int(self.current_sprite)+41]
#             self.rect.center = [self.x, self.y]
#             if self.current_sprite >= 50:
#                 self.current_sprite = 44
            
                    
    def is_clicked(self):
        return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())