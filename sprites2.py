from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from config_trabalho import *

jogador = Sprite("r_sheet.png", 44)           #idle, direita, esquerda, costa, frente
jogador.set_sequence(1, 8,  loop=True)
jogador.set_total_duration(6000)
jogador.x = 440
jogador.y = 480 #(meio)

jogador2 = Sprite("a_sheet.png", 44)
jogador2.set_sequence(1, 8, loop=True)
jogador2.set_total_duration(6000)
jogador2.x = 880
jogador2.y = 480