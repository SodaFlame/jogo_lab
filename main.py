from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from objects import *
from config_trabalho import *
from sprites import *
import math

mapa1 = GameImage("mapa_print.png")
janela = Window(width, height)
teclado = Window.get_keyboard()
mouse = Window.get_mouse()

right = False                    #isso eh feio mas eu preciso disso pras animacoes nao congelarem
left = False
up = False
down = False

while True:
    
    if (teclado.key_pressed("d")) and jogador.x < width:                      #esses ifs servem pra atualizar a animacao do personagem
        left = False
        up = False
        down = False
        
        if right == False:
            jogador.set_sequence(9, 17, loop=True)
            right = True
            
        jogador.x = jogador.x + velK * janela.delta_time()
        
    elif (teclado.key_pressed("a")) and jogador.x > 0:
        right = False
        up = False
        down = False
        
        if left == False:
            jogador.set_sequence(18, 26, loop=True)
            left = True
            
        jogador.x = jogador.x - velK * janela.delta_time()
    
    elif (teclado.key_pressed("w")) and jogador.y > 0:
        left = False
        right = False
        down = False
        
        if up == False:
            jogador.set_sequence(27, 35, loop=True)
            up = True
            
        jogador.y = jogador.y - velK * janela.delta_time()
        
    elif (teclado.key_pressed("s")) and jogador.y < height:
        left = False
        right = False
        up = False
        
        if down == False:
            jogador.set_sequence(36, 44, loop=True)
            down = True
            
        jogador.y = jogador.y + velK * janela.delta_time()
        
        
    for x in range(len(inimigos)):                             #passa o inimigo que ta colidindo com o jogador para uma lista
        if jogador.collided(inimigos[x][0]):
            selected.append(inimigos[x])
            break
    
    if len(selected) > 0:
        if jogador.collided(selected[0][0]) and mouse.is_button_pressed(1):    #se o jogador atacou, o inimigo perde vida
            print("attack")
            selected[0][1] -= 10
    
        if selected[0][1] <= 0 and selected[0] in inimigos:
            inimigos.remove(selected[0])
            selected.clear()
        
    else:
        selected.clear()
    
    for x in range(len(inimigos)):
        if math.sqrt((inimigos[x][0].x - jogador.x)**2 + (inimigos[x][0].y - jogador.y)**2) <= 100:           #faz com que o inimigo se mova em direcao ao jogador se ele chegar perto
            if inimigos[x][0].x > jogador.x:
                inimigos[x][0].x -= velM * janela.delta_time()
            if inimigos[x][0].x < jogador.x:
                inimigos[x][0].x += velM * janela.delta_time()
            if inimigos[x][0].y > jogador.y:
                inimigos[x][0].y -= velM * janela.delta_time()
            if inimigos[x][0].y < jogador.y:
                inimigos[x][0].y += velM * janela.delta_time()
            
            if inimigos[x][0].collided(jogador):
                print("attacked")
                print(inimigos[x][1])
    
    
    for x in range(len(objects)):
        if jogador.collided(objects[x]):
            obj_selected.append(objects[x])
            print('collided')
            break
    
    
    mapa1.draw()
    
    for x in range(len(objects)):
        objects[x].draw()
        
    for x in range(len(inimigos)):
        inimigos[x][0].draw()
        inimigos[x][0].update()
    
    jogador.draw()
    jogador.update()
    
    janela.update()
    
