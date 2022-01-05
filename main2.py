from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.collision import *
from objects2 import *
from config2 import *
from sprites2 import *
import math

janela = Window(width, height)
teclado = Window.get_keyboard()
mouse = Window.get_mouse()

right = False
left = False

while True:
    
    if (teclado.key_pressed("d")) and jogador.x < width:                      #esses ifs servem pra atualizar a animacao do personagem
        left = False
        
        if right == False:
            jogador.set_sequence(9, 17, loop=True)
            right = True
            
        jogador.x = jogador.x + velX * janela.delta_time()
        
    elif (teclado.key_pressed("a")) and jogador.x > 0:
        right = False
        
        if left == False:
            jogador.set_sequence(18, 26, loop=True)
            left = True
            
        jogador.x = jogador.x - velX * janela.delta_time()
    
    if jogador.collided(mapa1) == False:
        jogador.y += 80 * janela.delta_time()
    
    if jogador.collided(mapa1) and (teclado.key_pressed("space")):
        jogador.y -= 500*janela.delta_time()
    
    janela.set_background_color((0, 0, 0))
    jogador.draw()
    jogador.update()
    mapa1.draw()
    janela.update()
    

