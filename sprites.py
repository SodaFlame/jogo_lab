from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from config_trabalho import *

jogador = Sprite("r_sheet.png", 44)           #idle, direita, esquerda, costa, frente
jogador.set_sequence(1, 8,  loop=True)
jogador.set_total_duration(6000)
jogador.x = 10
jogador.y = 480 #(meio)

#inimigos

k1 = Sprite("r_sheet.png", 44)           #idle, direita, esquerda, costa, frente
k1.set_sequence(1, 8,  loop=True)
k1.set_total_duration(5000)
k1.x = 100
k1.y = 100

k2 = Sprite("r_sheet.png", 44)           #idle, direita, esquerda, costa, frente
k2.set_sequence(1, 8,  loop=True)
k2.set_total_duration(5000)
k2.x = 100
k2.y = 150

k3 = Sprite("azul_sheet.png", 44)           #idle, direita, esquerda, costa, frente
k3.set_sequence(1, 8,  loop=True)
k3.set_total_duration(5000)
k3.x = 100
k3.y = 100

k4 = Sprite("azul_sheet.png", 44)           #idle, direita, esquerda, costa, frente
k4.set_sequence(1, 8,  loop=True)
k4.set_total_duration(5000)
k4.x = 100
k4.y = 150

k5 = Sprite("azul_sheet.png", 44)           #idle, direita, esquerda, costa, frente
k5.set_sequence(1, 8,  loop=True)
k5.set_total_duration(5000)
k5.x = 100
k5.y = 200

k6 = Sprite("azul_sheet.png", 44)           #idle, direita, esquerda, costa, frente
k6.set_sequence(1, 8,  loop=True)
k6.set_total_duration(5000)
k6.x = 100
k6.y = 250

k7 = Sprite("azul_sheet.png", 44)           #idle, direita, esquerda, costa, frente
k7.set_sequence(1, 8,  loop=True)
k7.set_total_duration(5000)
k7.x = 100
k7.y = 300

k8 = Sprite("azul_sheet.png", 44)           #idle, direita, esquerda, costa, frente
k8.set_sequence(1, 8,  loop=True)
k8.set_total_duration(5000)
k8.x = 100
k8.y = 350


inimigos = [[k3, 60, 15, 10, 1], [k4, 60, 15, 10, 1], [k5, 60, 15, 10, 1], [k6, 60, 15, 10, 1], [k7, 60, 15, 10, 1], [k8, 60, 15, 10, 1]]
aliados = [[k1,30,15,10, 1], [k2,30,15,10, 1]]    #sprite, vida, ataque, defesa, ja se moveu?
selected = []
enemy_selected = []

init = 0

