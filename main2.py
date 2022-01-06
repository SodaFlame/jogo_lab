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

right1 = False
right2 = False
left1 = False
left2 = False

while True:
    
    #movimento
    
    if (teclado.key_pressed("d")) and jogador.x < width:                      #esses ifs servem pra atualizar a animacao do personagem
        left1 = False
        
        if right1 == False:
            jogador.set_sequence(9, 17, loop=True)
            right1 = True
            
        jogador.x = jogador.x + velX * janela.delta_time()
        
    elif (teclado.key_pressed("a")) and jogador.x > 0:
        right1 = False
        
        if left1 == False:
            jogador.set_sequence(18, 26, loop=True)
            left1 = True
            
        jogador.x = jogador.x - velX * janela.delta_time()
    
    if jogador.collided(jogador2):
        if teclado.key_pressed('h') and jogador.x > jogador2.x:
            jogador2.x -= 50
        elif teclado.key_pressed('h') and jogador.x < jogador2.x:
            jogador2.x += 50
    
    #jogador2
    if (teclado.key_pressed("right")) and jogador2.x < width:                      #esses ifs servem pra atualizar a animacao do personagem
        left2 = False
        
        if right2 == False:
            jogador2.set_sequence(9, 17, loop=True)
            right2 = True
            
        jogador2.x = jogador2.x + velX * janela.delta_time()
        
    elif (teclado.key_pressed("left")) and jogador2.x > 0:
        right2 = False
        
        if left2 == False:
            jogador2.set_sequence(18, 26, loop=True)
            left2 = True
            
        jogador2.x = jogador2.x - velX * janela.delta_time()
    
    
    
    if jogador.y > height or jogador.x > width or jogador.x < 0:
        jogador.y = 500
        jogador.x = width/2
        grav = 20
    
    if jogador2.y > height or jogador2.x > width or jogador2.x < 0:
        jogador2.y = 500
        jogador2.x = width/2
        grav2 = 20
    
    
    
    #colisoes
        
    if (jogador.collided(mapa1) and (jogador.y + 60) < mapa1.y) or (jogador.collided(p1) and (jogador.y + 60) < p1.y) or (jogador.collided(p2) and (jogador.y + 60) < p2.y):     #60 eh o offset do bloco principal, sla por que
        grav = 20
        jump_timer = 0
        
        if (teclado.key_pressed("space")):
            while jump_timer < jump_limit:
                jump_timer += 0.1
                jogador.y -= velY * janela.delta_time() * 0.2
            
    
    elif (jogador.collided(mapa1) and (jogador.y + 70) < mapa1.y) == False:
        if grav < gravL:
            grav *= 1.04
            
        jogador.y += grav*janela.delta_time()
                 
    
    if jogador.collided(mapa1) or jogador.collided(p1) or jogador.collided(p2):
        if (jogador.y + 60 > mapa1.y and jogador.x < mapa1.x) or (jogador.y + 60 > p2.y and jogador.x > p2.x - p2.width):      #isso testa pra ver se ele ta de baixo da plataforma, e se ele ta indo contra a parede
            velX = 0
            jogador.x -= 5  #impede patinacao
        elif (jogador.y + 60 > mapa1.y and jogador.x > mapa1.x + mapa1.width-70) or (jogador.y + 60 > p2.y and jogador.x < p2.x + p2.width):        #mesma coisa soq pro outro lado
            velX = 0
            jogador.x += 5
        
        if (jogador.collided(mapa1) or jogador.collided(p1) or jogador.collided(p2)) == False:
            velX = 200
    
    if (jogador2.collided(mapa1) and (jogador2.y + 60) < mapa1.y) or (jogador2.collided(p1) and (jogador2.y + 60) < p1.y) or (jogador2.collided(p2) and (jogador2.y + 60) < p2.y):
        grav2 = 20
        jump_timer2 = 0
         
        if (teclado.key_pressed("j")):
             while jump_timer2 < jump_limit:
                 jump_timer2 += 0.1
                 jogador2.y -= velY * janela.delta_time() * 0.2
                 
        
    elif (jogador2.collided(mapa1) and (jogador2.y + 70) < mapa1.y) == False:
        if grav2 < gravL:
            grav2 *= 1.04
            
        jogador2.y += grav2*janela.delta_time()
            
            
    if jogador2.collided(mapa1) or jogador2.collided(p1) or jogador2.collided(p2):
        if (jogador2.y + 60 > mapa1.y and jogador2.x < mapa1.x) or (jogador2.y + 60 > p2.y and jogador2.x > p2.x - p2.width):      #isso testa pra ver se ele ta de baixo da plataforma, e se ele ta indo contra a parede
            velX2 = 0
            jogador2.x -= 5  #impede patinacao
        elif (jogador2.y + 60 > mapa1.y and jogador2.x > mapa1.x + mapa1.width-70) or (jogador2.y + 60 > p2.y and jogador2.x < p2.x + p2.width):        #mesma coisa soq pro outro lado
            velX2 = 0
            jogador2.x += 5
        
        if (jogador2.collided(mapa1) or jogador2.collided(p1) or jogador2.collided(p2)) == False:
            velX2 = 200
    
    
           
    janela.set_background_color((0, 0, 0))
    jogador.draw()
    jogador.update()
    jogador2.draw()
    jogador2.update()
    
    for x in range(len(objetos)):
        objetos[x].draw()
    
    janela.update()
    

