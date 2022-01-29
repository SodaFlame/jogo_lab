from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from config_trabalho import *

#bonecos

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

#menu

jogar = Sprite("jogar.png", frames=1)
jogar.x = width/2 - jogar.width/2
jogar.y = 200
configuracoes = Sprite("configuracoes.png", frames=1)
configuracoes.x = width/2 - configuracoes.width/2
configuracoes.y = 250
sair = Sprite("sair.png", frames=1)
sair.x = width/2 - sair.width/2
sair.y = 300
background = GameImage('sky.jpg')

#UI

healthbar1 = Sprite("healthbar_nobg.png", frames = 6)

healthbar2 = Sprite("healthbar_nobg.png", frames = 6)
healthbar2.x = width - healthbar2.width