from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from config_trabalho import *

jogador = Sprite("r_sheet.png", 44)           #idle, direita, esquerda, costa, frente
jogador.set_sequence(1, 8,  loop=True)
jogador.set_total_duration(6000)
jogador.x = 440
jogador.y = 480 #(meio)