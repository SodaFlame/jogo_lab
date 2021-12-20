from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from config_trabalho import *


k1 = Sprite("r_sheet.png", 44)           #idle, direita, esquerda, costa, frente
k1.set_sequence(1, 8,  loop=True)
k1.set_total_duration(5000)
k1.x = 900
k1.y = 900

k2 = Sprite("r_sheet.png", 44)           #idle, direita, esquerda, costa, frente
k2.set_sequence(1, 8,  loop=True)
k2.set_total_duration(5000)
k2.x = 300
k2.y = 300

k3 = Sprite("azul_sheet.png", 44)           #idle, direita, esquerda, costa, frente
k3.set_sequence(1, 8,  loop=True)
k3.set_total_duration(5000)
k3.x = 450
k3.y = 450

inimigos = [[k3, 30, 15, 10]]
aliados = [[k1,30,15,10], [k2,30,15,10]]    #sprite, vida, ataque, defesa
selected = []

moveK = 100000

