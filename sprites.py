import pygame as pg
import spriteclass
from pygame.locals import *

number_of_animations = 9
black = (0, 0, 0)

azul_idl = pg.image.load('azul_idle.png')
azul_idle = spriteclass.spritesheet(azul_idl)
az_idl_ls = []

az_fr_an = pg.image.load('azul_frente_andando.png')
azul_frente_andando = spriteclass.spritesheet(az_fr_an)
az_fr_ls = []

az_di_an = pg.image.load('azul_direita.png')
azul_direita_andando = spriteclass.spritesheet(az_di_an)
az_di_ls = []

az_es_an = pg.image.load('azul_esquerda.png')
azul_esquerda_andando = spriteclass.spritesheet(az_es_an)
az_es_ls = []

az_co_an = pg.image.load('azul_costa.png')
azul_costa_andando = spriteclass.spritesheet(az_co_an)
az_co_ls = []

def AppendSprites(number_of_animations, target_list, spritesheet): #put sprites in a list instead of having to write a clusterfuck of code
    for x in range(number_of_animations):
        target_list.append(spritesheet.get_sprite(x, 64, 64, 1, black))

AppendSprites(9, az_es_ls, azul_esquerda_andando)
AppendSprites(9, az_di_ls, azul_direita_andando)
AppendSprites(8, az_idl_ls, azul_idle)
AppendSprites(9, az_co_ls, azul_costa_andando)
AppendSprites(9, az_fr_ls, azul_frente_andando)

todas_sprites_knight = az_idl_ls + az_fr_ls + az_di_ls + az_es_ls + az_co_ls #idle, frente, direita, esquerda, costa: (0-7, 8-16, 17-25, 26-34, 35-43)


