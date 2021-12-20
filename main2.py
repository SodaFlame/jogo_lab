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

lv1 = False
clicked = False

while True: #main loop
    
    lv1 = True
    
    if lv1:
        #control characters
                
        if is_clicked() != None:
            selected.append(is_clicked())
        
        if len(selected) > 0:
            
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
                if math.sqrt((selected[0][0].x - inimigos[x][0].x)**2 + (selected[0][0].y - inimigos[x][0].y)**2) < 60 and mouse.is_button_pressed(1): #colocar animacao de ataque aqui
                    inimigos[x][1] -= (selected[0][2])/2       #quem foi atacado perde hp
                    print(inimigos[x][1])
                    
                    if inimigos[x][1] <= 0:
                        inimigos.remove(inimigos[x])
                    break
                    
            
            if mouse.is_button_pressed(3):
                selected.clear()
            
            
        
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
    
