#implement a turn-based system (OK)
#implement basic AI (to-do)

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

def is_clicked():
    for x in range(len(aliados)):
        if mouse.is_over_object(aliados[x][0]) and  mouse.is_button_pressed(1):
            return aliados[x]

def enemy_move():
    for x in range(len(inimigos)):
        if inimigos[x][4] == 1:
            return inimigos[x]

lv1 = False
clicked = False
amount_of_moves = len(aliados)

while True: #main loop
    
    lv1 = True
    
    if lv1:
        #control characters
                
        if is_clicked() != None and amount_of_moves > 0:                         #Vez do jogador
            selected.append(is_clicked())
        
        if len(selected) > 0 and selected[0][4] == 1:
            
            if (teclado.key_pressed("w")) and k1.y > 0:
                selected[0][0].y = selected[0][0].y - velK * janela.delta_time()
                moveK -=10
            if (teclado.key_pressed("s")) and k1.y < height:
                selected[0][0].y = selected[0][0].y + velK * janela.delta_time()
                moveK -= 10
            if (teclado.key_pressed("a")) and k1.x > 0:
                selected[0][0].set_initial_frame(30)
                selected[0][0].set_final_frame(40)
                moveK -= 10
                selected[0][0].x = selected[0][0].x - velK * janela.delta_time()
            if (teclado.key_pressed("d")) and k1.x < width:
                selected[0][0].x = selected[0][0].x + velK * janela.delta_time()
                moveK -= 10
            
            for x in range(len(inimigos)):
                if selected[0][0].collided(inimigos[x][0]):
                    enemy_selected.append(inimigos[x])
            
            if len(enemy_selected) > 0:
                if math.sqrt((selected[0][0].x - enemy_selected[0][0].x)**2 + (selected[0][0].y - enemy_selected[0][0].y)**2) < 60 and mouse.is_button_pressed(1): #colocar animacao de ataque aqui
                    enemy_selected[0][1] -= (selected[0][2])       #quem foi atacado perde hp
                    print(enemy_selected[0][1])
                    amount_of_moves -= 1
                    selected[0][4] = 0
                    selected.clear()
                
                    if enemy_selected[0][1] <= 0:                    #se o hp cair pra 0, remover o personagem da lista
                        inimigos.remove(enemy_selected[0])
                    
                    enemy_selected.clear()
                       
            if mouse.is_button_pressed(3):
                selected.clear()
                
        if amount_of_moves <= 0:                               #Vez do inimigo
            for x in range(len(inimigos)):
                if inimigos[x][4] == 1:
                    enemy_selected.append(inimigos[x])
                    
            
            for x in range(len(aliados)):
                if enemy_selected[0][0].x > aliados[x][0].x:
                    enemy_selected[0][0].x -= velK*janela.delta_time()
                if enemy_selected[0][0].x < aliados[x][0].x:
                    enemy_selected[0][0].x += velK*janela.delta_time()
                if enemy_selected[0][0].y < aliados[x][0].y:
                    enemy_selected[0][0].y += velK*janela.delta_time()
                if enemy_selected[0][0].y > aliados[x][0].y:
                    enemy_selected[0][0].y -= velK*janela.delta_time()
                    
                
            amount_of_moves = len(aliados)
            for x in range(len(aliados)):
                aliados[x][4] = 1
            
        #draw everything
                
        mapa1.draw()
        fl1.draw()
        fl2.draw()
        loja1.draw()
        loja2.draw()
        
        for x in range(len(aliados)):
            aliados[x][0].draw()
            aliados[x][0].update()
        
        for x in range (len(inimigos)):
            inimigos[x][0].draw()
            inimigos[x][0].update()
        
    janela.update()
    
