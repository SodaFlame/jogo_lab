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
            jogador2HP -= 30
        elif teclado.key_pressed('h') and jogador.x < jogador2.x and atk_counter >= 0.8 and airbone == False:
            atk_counter = 0
            jogador2.x += 50
            jogador2HP -= 30
        if teclado.key_pressed('j') and jogador.x > jogador2.x and atk_counter >= 1.2 and airbone == False:
            atk_counter = 0
            jogador2.x -= 80
            jogador2HP -= 50
        elif teclado.key_pressed('j') and jogador.x < jogador2.x and atk_counter >= 1.2 and airbone == False:
            atk_counter = 0
            jogador2.x += 80
            jogador2HP -= 50
    
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
    
    if jogador2.y > height or jogador2.x > width or jogador2.x < 0 or jogador2HP <= 0:
        jogador2.y = 500
        jogador2.x = width/2
        grav2 = 20
        velX2 = 200
        velY2 = 5
        jogador2HP = 1000
    
    
    
    #colisoes e outros movimentos
    
    if len(selected_obj) == 0:
        for x in range(len(objetos)):
            if jogador.collided(objetos[x]):
                selected_obj.append(objetos[x])
                if jogador.y + 50 < selected_obj[0].y:
                    grav = 20
                    jump_timer = 0
    
    if len(selected_obj) > 0:
        if jogador.collided(selected_obj[0]) and jogador.y + 50 < selected_obj[0].y:
            airbone = False
            if (teclado.key_pressed("space")):
                while jump_timer < jump_limit:
                    jump_timer += 0.01
                    jogador.y -= velY * janela.delta_time() * 0.2
        
                    
        if (jogador.y + 50  > selected_obj[0].y and jogador.x < selected_obj[0].x):      #isso testa pra ver se ele ta de baixo da plataforma, e se ele ta indo contra a parede
            velX = 0
            jogador.x -= 10  #impede patinacao
        
        if (jogador.y + 50 > selected_obj[0].y and jogador.x > selected_obj[0].x):   
            velX = 0
            jogador.x += 10
        
        if jogador.y + 60 < selected_obj[0].y:
            if grav < gravL:
                grav *= 1.04
            jogador.y += janela.delta_time()*grav
        
        if jogador.collided(selected_obj[0]) == False:
            velX = 200
            selected_obj.clear()
    
    if len(selected_obj) == 0:
        if grav < gravL:
            grav *= 1.04
        jogador.y += janela.delta_time()*grav
        airbone = True
    
    
    #jogador2
        
    if len(selected_obj2) == 0:
        for x in range(len(objetos)):
            if jogador2.collided(objetos[x]):
                selected_obj2.append(objetos[x])
                if jogador2.y + 60 < selected_obj2[0].y:
                    grav2 = 20
                    jump_timer2 = 0
        
    if len(selected_obj2) > 0:
        airbone2 = False
        if jogador2.collided(selected_obj2[0]) and jogador2.y + 50 < selected_obj2[0].y:
            if (teclado.key_pressed("l")):
                while jump_timer2 < jump_limit:
                    jump_timer2 += 0.01
                    jogador2.y -= velY2 * janela.delta_time() * 0.2
        
                    
        if (jogador2.y + 50  > selected_obj2[0].y and jogador2.x < selected_obj2[0].x):     
            velX2 = 0
            jogador2.x -= 10 
        
        if (jogador2.y + 50 > selected_obj2[0].y and jogador2.x > selected_obj2[0].x):   
            velX2 = 0
            jogador2.x += 10
        
        if jogador2.y + 60 < selected_obj2[0].y:
            if grav2 < gravL:
                grav2 *= 1.04
            jogador2.y += janela.delta_time()*grav2
        
        if jogador2.collided(selected_obj2[0]) == False:
            velX2 = 200
            selected_obj2.clear()
    
    if len(selected_obj2) == 0:
        if grav2 < gravL:
            grav2 *= 1.04
        jogador2.y += janela.delta_time()*grav2
        airbone2 = True
    
    print(airbone)
    
    
        

           
    janela.set_background_color((0, 0, 0))
    jogador.draw()
    jogador.update()
    jogador2.draw()
    jogador2.update()
    
    for x in range(len(objetos)):
        objetos[x].draw()
    
    janela.update()
    

