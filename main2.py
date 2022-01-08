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
airbone = False                     #essas 2 ultimas booleanas determinam se o personagem ta no ar ou n
airbone2 = False 

while True:
    
    atk_counter += janela.delta_time()                 #timer pros ataques dos personagens
    atk_counter2 += janela.delta_time()
    
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
        if teclado.key_pressed('h') and jogador.x > jogador2.x and atk_counter >= 0.8 and airbone == False:
            atk_counter = 0
            jogador2.x -= 50
        elif teclado.key_pressed('h') and jogador.x < jogador2.x and atk_counter >= 0.8 and airbone == False:
            atk_counter = 0
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
    
    
    
    if jogador.y > height or jogador.x > width or jogador.x < 0:                   #reseta o jogador se ele cair pra fora do mapa
        jogador.y = 500
        jogador.x = width/2
        grav = 20
        velX = 200
        velY = 5
    
    if jogador2.y > height or jogador2.x > width or jogador2.x < 0:
        jogador2.y = 500
        jogador2.x = width/2
        grav2 = 20
        velX2 = 200
        velY2 = 5
    
    
    
    #colisoes e outros movimentos
        
    if (jogador.collided(plat1) and (jogador.y + 60) < plat1.y) or (jogador.collided(plat2) and (jogador.y + 60) < plat2.y) or (jogador.collided(p1) and (jogador.y + 60) < p1.y) or (jogador.collided(p2) and (jogador.y + 60) < p2.y):     #60 eh o offset do bloco principal, sla por que
        grav = 20
        jump_timer = 0
        
        if (teclado.key_pressed("space")):
            while jump_timer < jump_limit:
                jump_timer += 0.01
                jogador.y -= velY * janela.delta_time() * 0.02
            
    
    elif (jogador.collided(plat1) and (jogador.y + 70) < plat1.y) == False:
        if grav < gravL:
            grav *= 1.04
            
        jogador.y += grav*janela.delta_time()
                 
    
    if jogador.collided(plat1) or jogador.collided(p1) or jogador.collided(p2):
        airbone = False
        if (jogador.y + 60 > plat1.y and jogador.x < plat1.x) or (jogador.y + 60 > p2.y and jogador.x > p2.x - p2.width):      #isso testa pra ver se ele ta de baixo da plataforma, e se ele ta indo contra a parede
            velX = 0
            jogador.x -= 10  #impede patinacao
        elif (jogador.y + 60 > plat1.y and jogador.x > plat1.x + plat1.width-70) or (jogador.y + 60 > p2.y and jogador.x < p2.x + p2.width):        #mesma coisa soq pro outro lado
            velX = 0
            jogador.x += 10
    
    if jogador.collided(plat2):                                                  #se eu n lidar com as colisoes das 2 plataformas separadamente da patinacao, sabe-se la pq
        airbone = False
        if (jogador.y + 60 > plat2.y and jogador.x < plat2.x):
            velX = 0
            jogador.x -= 10
        elif (jogador.y + 60 > plat2.y and jogador.x > plat2.x + plat1.width-70):
            velX = 0
            jogador.x += 10
            
        
    if jogador.collided(plat1) == False and jogador.collided(plat2) == False and jogador.collided(p1) == False  and  jogador.collided(p2) == False:         #n tem como passar isso pra uma funcao n?
        airbone = True
        velX = 200
    
#     if jogador.collided(fl1) and (jogador.y + 20 < fl1.y):
#         if 
#             
    
    
    #jogador2
    if (jogador2.collided(plat1) and (jogador2.y + 60) < plat1.y) or (jogador2.collided(plat2) and (jogador2.y + 60) < plat2.y) or (jogador2.collided(p1) and (jogador2.y + 60) < p1.y) or (jogador2.collided(p2) and (jogador2.y + 60) < p2.y):     #60 eh o offset do bloco principal, sla por que
        grav2 = 20
        jump_timer2 = 0
        
        if (teclado.key_pressed("j")):
            while jump_timer2 < jump_limit:
                jump_timer2 += 0.01
                jogador2.y -= velY2 * janela.delta_time() * 0.02
            
    
    elif (jogador2.collided(plat1) and (jogador2.y + 70) < plat1.y) == False:
        if grav2 < gravL:
            grav2 *= 1.04
            
        jogador2.y += grav2*janela.delta_time()
                 
    
    if jogador2.collided(plat1) or jogador2.collided(p1) or jogador2.collided(p2):
        airbone = False
        if (jogador2.y + 60 > plat1.y and jogador2.x < plat1.x) or (jogador2.y + 60 > p2.y and jogador2.x > p2.x - p2.width):     
            velX2 = 0
            jogador2.x -= 10  #impede patinacao
        elif (jogador2.y + 60 > plat1.y and jogador2.x > plat1.x + plat1.width-70) or (jogador2.y + 60 > p2.y and jogador2.x < p2.x + p2.width):        
            velX2 = 0
            jogador2.x += 10
    
    if jogador2.collided(plat2):                                                 
        airbone = False
        if (jogador2.y + 60 > plat2.y and jogador2.x < plat2.x):
            velX2 = 0
            jogador2.x -= 10
        elif (jogador2.y + 60 > plat2.y and jogador2.x > plat2.x + plat1.width-70):
            velX2 = 0
            jogador2.x += 10
        
        
    if jogador2.collided(plat1) == False and jogador2.collided(plat2) == False and jogador2.collided(p1) == False  and  jogador2.collided(p2) == False:         
        airbone = True
        velX2 = 200
    
    #movimentacao de objetos
    
    fl1.y -= janela.delta_time() * velFl
    fl2.y += janela.delta_time() * velFl
    
    if fl1.y <= 200 or fl1.y >= 1000:
        velFl *= -1
    
    
    
    

           
    janela.set_background_color((0, 0, 0))
    jogador.draw()
    jogador.update()
    jogador2.draw()
    jogador2.update()
    
    for x in range(len(objetos)):
        objetos[x].draw()
    
    janela.update()
    

