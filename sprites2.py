from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from config2 import *

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
jogar.y = 300
configuracoes = Sprite("configuracoes.png", frames=1)
configuracoes.x = width/2 - configuracoes.width/2
configuracoes.y = 350
sair = Sprite("sair.png", frames=1)
sair.x = width/2 - sair.width/2
sair.y = 400
lv1 = GameImage('lv1.png')
lv1.x = width/2 - lv1.width/2
lv1.y = 100
lv2 = GameImage('lv2.png')
lv2.x = width/2 - lv2.width/2
lv2.y = 150

#UI

healthbar1 = Sprite("healthbar_nobg.png", frames = 6)

healthbar2 = Sprite("healthbar_nobg.png", frames = 6)
healthbar2.x = width - healthbar2.width

heartbar = []
heartbar2 = []
heartbar3 = []
heartbar4 = []

for x in range(jogador_vida):
    heartbar.append(GameImage('full_heart.png'))
    heartbar[x].x = 10 + (heartbar[x].width*1.1*x)
    heartbar[x].y = 40
    heartbar2.append(GameImage('empty_heart.png'))
    heartbar2[x].x = 10 + (heartbar[x].width*1.1*x)
    heartbar2[x].y = 40

for x in range(jogador2_vida):
    heartbar3.append(GameImage('full_heart.png'))
    heartbar3[x].x = width - 10 - heartbar3[x].width - (heartbar3[x].width*1.1*x)
    heartbar3[x].y = 40
    heartbar4.append(GameImage('empty_heart.png'))
    heartbar4[x].x = width - 10 - heartbar3[x].width - (heartbar3[x].width*1.1*x)
    heartbar4[x].y = 40
    