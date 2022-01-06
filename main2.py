from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.collision import *
from objects2 import *
from config2 import *
from sprites2 import *

janela = Window(width, height)
teclado = Window.get_keyboard()
mouse = Window.get_mouse()

right = False
left = False
standing = True

while True:
    
    #movimento
    
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
    
    
    
    #colisoes
        
    if jogador.collided(mapa1) and (jogador.y + 60) < mapa1.y:      #60 eh o offset do bloco principal, sla por que
        standing = True
        grav = 20
        if (teclado.key_pressed("space")):
            jogador.y -= 40
            jogador.y -= 500*janela.delta_time()
    
    elif (jogador.collided(mapa1) and (jogador.y + 70) < mapa1.y) == False:
        grav *= 1.05
        jogador.y += grav*janela.delta_time()
    
    print(mapa1.x + mapa1.width, jogador.x)
    if jogador.collided(mapa1):
        if ((jogador.y + 60) > mapa1.y) and jogador.x < mapa1.x and teclado.key_pressed("d"):             #isso testa pra ver se ele ta de baixo da plataforma, e se ele ta indo contra a parede
            velX = 0
        elif ((jogador.y + 60) > mapa1.y) and jogador.x > (mapa1.x + mapa1.width-70) and teclado.key_pressed("a"):            #mesma coisa soq pro outro lado
            velX = 0
        else:
            velX = 200
    
    

            
            
    
           
    
    janela.set_background_color((0, 0, 0))
    jogador.draw()
    jogador.update()
    
    for x in range(len(objetos)):
        objetos[x].draw()
    
    janela.update()
    

