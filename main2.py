from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.collision import *
from objects2 import *
from config2 import *
from sprites2 import *
import random

janela = Window(width, height)
teclado = Window.get_keyboard()
mouse = Window.get_mouse()

right1 = False
right2 = False
left1 = False
left2 = False
airbone = False                     #essas 2 ultimas booleanas determinam se o personagem ta no ar ou n
airbone2 = False
jumping = False
jumping2 = False
in_selection = False
in_game = False
in_menu = False

while True:
    
    in_menu = True
    
    while in_menu:

        janela.set_background_color((0, 0, 0))
        jogar.draw()
        configuracoes.draw()
        sair.draw()
        janela.draw_text("Superfighters", width/2 - 130, 50, size=40, color = (255, 255, 0), font_name = 'Comic Sans', bold = False, italic = False)
        janela.update()

        if mouse.is_over_object(sair) and mouse.is_button_pressed(1):
            janela.close()
        if mouse.is_over_object(jogar) and mouse.is_button_pressed(1):
            in_selection = True
            in_menu = False
        
    while in_selection:
        if mouse.is_over_object(lv1) and mouse.is_button_pressed(1):
            is_lv2 = 0
            in_game = True
            in_selection = False
        
        if mouse.is_over_object(lv2) and mouse.is_button_pressed(1):
            is_lv2 = 1
            plat1 = GameImage('plat1.png')
            plat1.x = width/2 - plat1.width/2
            plat1.y = 650
            
            p1 = GameImage('small_plat1.png')
            p1.x = plat1.x + 50
            p1.y = 450
            
            p2 = GameImage('small_plat1.png')
            p2.x = (plat1.x + plat1.width) - 50 - p2.width
            p2.y = 450
            
            p3 = GameImage('small_plat1.png')
            p3.x = plat1.x + plat1.width/2 - p3.width/2
            p3.y = 300
            
            
            objetos = [plat1, p1, p2, p3]
            pw_coords = [[plat1.x, plat1.y],[p1.x, p1.y],[p2.x, p2.y],[p3.x, p3.y]]
            in_game = True
            in_selection = False
        
        janela.set_background_color((0, 0, 0))
        lv1.draw()
        lv2.draw()
        janela.update()
        
    while in_game:
        time_elapsed += janela.delta_time()
        atk_counter += janela.delta_time()                 #timer pros ataques dos personagens
        atk_counter2 += janela.delta_time()
        if teclado.key_pressed('ESC'):
            break
        
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
            if teclado.key_pressed('h') and jogador.x > jogador2.x and atk_counter >= 0.8:
                atk_counter = 0
                jogador2.x -= 50
                jogador2HP -= 30*atk1
            elif teclado.key_pressed('h') and jogador.x < jogador2.x and atk_counter >= 0.8:
                atk_counter = 0
                jogador2.x += 50
                jogador2HP -= 30*atk1
            if teclado.key_pressed('j') and jogador.x > jogador2.x and atk_counter >= 1.2:
                atk_counter = 0
                jogador2.x -= 80
                jogador2HP -= 50*atk1
            elif teclado.key_pressed('j') and jogador.x < jogador2.x and atk_counter >= 1.2:
                atk_counter = 0
                jogador2.x += 80
                jogador2HP -= 50*atk1
        
        if jogador2.collided(jogador):
            if teclado.key_pressed('m') and jogador2.x > jogador.x and atk_counter2 >= 0.8:
                atk_counter2 = 0
                jogador.x -= 50
                jogadorHP -= 30*atk2
            elif teclado.key_pressed('m') and jogador2.x < jogador.x and atk_counter2 >= 0.8:
                atk_counter2 = 0
                jogador.x += 50
                jogadorHP -= 30*atk2
            if teclado.key_pressed('n') and jogador2.x > jogador.x and atk_counter2 >= 1.2:
                atk_counter2 = 0
                jogador.x -= 80
                jogadorHP -= 50*atk2
            elif teclado.key_pressed('n') and jogador2.x < jogador.x and atk_counter2 >= 1.2:
                atk_counter2 = 0
                jogador.x += 80
                jogadorHP -= 50*atk2


        #healthbar

        if 1000 >= jogadorHP >= 800:         #as frames tao bugadas, nao me pergunte pq
            healthbar1.set_curr_frame(5)
        if 800 > jogadorHP > 600:
            healthbar1.set_curr_frame(4)
        if 600 > jogadorHP > 400:
            healthbar1.set_curr_frame(3)
        if 400 > jogadorHP > 200:
            healthbar1.set_curr_frame(2)
        if 200 > jogadorHP > 0:
            healthbar1.set_curr_frame(1)
            

            

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

        if 1000 >= jogador2HP >= 800:      #as frames tao bugadas, nao me pergunte pq
            healthbar2.set_curr_frame(5)
        if 800 > jogador2HP > 600:
            healthbar2.set_curr_frame(4)
        if 600 > jogador2HP > 400:
            healthbar2.set_curr_frame(3)
        if 400 > jogador2HP > 200:
            healthbar2.set_curr_frame(2)
        if 200 > jogador2HP > 0:
            healthbar2.set_curr_frame(1)



        if jogador.y > height or jogador.x > width or jogador.x < 0:                   #reseta o jogador se ele cair pra fora do mapa
            jogador.y = 500
            jogador.x = width/2
            grav = 20
            velX = 200
            velY = 5
            jogadorHP = 1000
            atk1 = 1
            jogador_vida -= 1
            heartbar.pop(jogador_vida)

        if jogador2.y > height or jogador2.x > width or jogador2.x < 0 or jogador2HP <= 0:
            jogador2.y = 500
            jogador2.x = width/2
            grav2 = 20
            velX2 = 200
            velY2 = 5
            jogador2HP = 1000
            atk2 = 1
            jogador2_vida -= 1
            heartbar3.pop(jogador2_vida)
        
        if jogador2_vida == 0 or jogador_vida == 0:
            break

        #colisoes e outros movimentos

        if len(selected_obj) == 0:                
            for x in range(len(objetos)):
                if jogador.collided(objetos[x]):
                    selected_obj.append(objetos[x])
                    if jogador.y + 40 < selected_obj[0].y:
                        grav = 20
                        jump_timer = 0

        if len(selected_obj) > 0:                                                            #esse pulo ta me matando. Eu n sei pq ele ta indo instantaneamente, isso ta fodendo cm as colisoes todas, e fica feio
            if jogador.collided(selected_obj[0]) and jogador.y + 50 < selected_obj[0].y:
                airbone = False
                jumping = False
                if (teclado.key_pressed("space")):
                        jumping = True
            
            if (jogador.y + jogador.height/6) > (selected_obj[0].y + selected_obj[0].height):
                velY = 0
                jump_timer = jump_limit
                jogador.y += 20
                        
            if (jogador.y + 50  > selected_obj[0].y and jogador.x < selected_obj[0].x) and jumping == False:     #isso testa pra ver se ele ta de baixo da plataforma, e se ele ta indo contra a pared            velX = 0
                jogador.x -= 10  #impede patinacao
            
            if (jogador.y + 50 > selected_obj[0].y and jogador.x > selected_obj[0].x) and jumping == False:  
                velX = 0
                jogador.x += 10
            
            if jogador.y + 60 < selected_obj[0].y:
                if grav < gravL:
                    grav *= 1.04
                jogador.y += janela.delta_time()*grav
            
            if jogador.collided(selected_obj[0]) == False:
                velY = 5
                velX = 200
                selected_obj.clear()

        if len(selected_obj) == 0 and jumping == False:
            if grav < gravL:
                grav *= 1.04
            jogador.y += janela.delta_time()*grav
            airbone = True

        if jumping:
            jump_timer += 8
            jogador.y -= 20*janela.delta_time()*25
            if jump_timer >= jump_limit:
                jumping = False
                jump_timer = 0


        #jogador2
            
        if len(selected_obj2) == 0:
            for x in range(len(objetos)):
                if jogador2.collided(objetos[x]):
                    selected_obj2.append(objetos[x])
                    if jogador2.y + 40 < selected_obj2[0].y:
                        grav2 = 20
                        jump_timer2 = 0
            
        if len(selected_obj2) > 0:
            airbone2 = False
            if jogador2.collided(selected_obj2[0]) and jogador2.y + 50 < selected_obj2[0].y:
                airbone2 = False
                jumping2 = False
                if (teclado.key_pressed("up")):
                        jumping2 = True
            
            if (jogador2.y + jogador2.height) > (selected_obj2[0].y + selected_obj2[0].height):
                velY2 = 0
                jogador2.y += 10
            
            elif (jogador2.y + 50  > selected_obj2[0].y and jogador2.x < selected_obj2[0].x):     
                velX2 = 0
                jogador2.x -= 10 
            
            elif (jogador2.y + 50 > selected_obj2[0].y and jogador2.x > selected_obj2[0].x):   
                velX2 = 0
                jogador2.x += 10
            
            if jogador2.y + 60 < selected_obj2[0].y:
                if grav2 < gravL:
                    grav2 *= 1.04
                jogador2.y += janela.delta_time()*grav2
            
            if jogador2.collided(selected_obj2[0]) == False:
                velX2 = 200
                velY2 = 5
                selected_obj2.clear()

        if len(selected_obj2) == 0:
            if grav2 < gravL:
                grav2 *= 1.04
            jogador2.y += janela.delta_time()*grav2
            airbone2 = True
        
        if jumping2:
            jump_timer2 += 6
            jogador2.y -= 20*janela.delta_time()*25
            if jump_timer2 >= jump_limit:
                jumping2 = False
                jump_timer2 = 0

        #spawn powerups
            
        if time_elapsed > 10 and amount_of_pw < pw_limit:
            if len(pw_random_coords) == 0:
                pw_random_coords = (random.sample(range(0, len(pw_coords)-1), pw_limit))   #determina as coordenadas do powerup, preciso desse controle pra impedir coordenada repetida
            if len(pw_random) == 0:
                pw_random = random.sample(range(0, len(pw_list)), len(pw_list))                  #decide qual powerup vai spawnar
                
            pw_spawned.append(pw_list[pw_random[current_pw]])
            pw_spawned.append(pw_coords[pw_random_coords[current_coords]])
            
            time_elapsed = 0
            amount_of_pw += 1          #controle pra quantidade de powerups
            current_coords += 1
            current_pw += 1
            
            if current_coords == pw_limit:      #reseta a rotacao de powerups quando ela termina
                current_coords = 0
                pw_random_coords.clear()
            if current_pw == len(pw_list):
                current_pw = 0

        #interaction with powerups (ta tando erro)

        if len(pw_spawned) > 1:                #isso ta uma zona mas a essa altura do campeonato minha paciencia ja foi pro inferno
            for x in range(len(pw_spawned)):
                if x % 2 == 0 and len(pw_collected) < 2:
                    if jogador.collided(pw_spawned[x]):
                        pw_collected.append(pw_spawned[x])
                        pw_collected.append(pw_spawned[x+1])
                        amount_of_pw -= 1
                        break
                    if jogador2.collided(pw_spawned[x]):
                        pw_collected2.append(pw_spawned[x])
                        pw_collected2.append(pw_spawned[x+1])
                        amount_of_pw -= 1
                        break


        if len(pw_collected) > 1:
            if pw_collected[0] == pw_atk:
                j1_pw_timer = 0
                atk1 = 1.5
            if pw_collected[0] == pw_hp:
                jogadorHP += 300
                if jogadorHP > 1000:
                    jogadorHP = 1000
                    
            pw_spawned.remove(pw_collected[0])
            pw_spawned.remove(pw_collected[1])
            pw_collected.clear()

        if len(pw_collected2) > 1:
            if pw_collected2[0] == pw_atk:
                j2_pw_timer = 0
                atk2 = 1.5
            if pw_collected2[0] == pw_hp:
                jogador2HP += 300
                if jogador2HP > 1000:
                    jogador2HP = 1000
                
                
                
            pw_spawned.remove(pw_collected2[0])
            pw_spawned.remove(pw_collected2[1])
            
            pw_collected2.clear()
                
        j1_pw_timer += janela.delta_time()
        if j1_pw_timer > 20:
            atk1 = 1

        j2_pw_timer += janela.delta_time()
        if j2_pw_timer > 20:
            atk2 = 1
            
            
            
        janela.set_background_color((0, 0, 0))
        jogador.draw()
        jogador.update()
        jogador2.draw()
        jogador2.update()

        healthbar1.draw()
        healthbar2.draw()

        for x in range(len(objetos)):
            objetos[x].draw()
        for x in range(len(heartbar)):
            heartbar[x].draw()
        for x in range(len(heartbar2)):
            heartbar2[x].draw()
        for x in range(len(heartbar3)):
            heartbar3[x].draw()
        for x in range(len(heartbar4)):
            heartbar4[x].draw()

        if len(pw_spawned) > 1:
            for x in range(len(pw_spawned)):
                if x % 2 == 0:                    #como eu to botando os powerups e coordenadas em uma lista so, eu preciso disso pra garantir que ele so chama o draw() pra GameImage
                    pw_spawned[x].draw()
                    pw_spawned[x].x = pw_spawned[x+1][0] 
                    pw_spawned[x].y = pw_spawned[x+1][1] - 64

        janela.update()






