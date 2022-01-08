from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from config2 import *

plat1 = GameImage("plat2.png")
plat1.x = width/2 - plat1.width/2
plat1.y = 600

plat2 = GameImage("plat2.png")
plat2.x = width/2 - plat1.width/2
plat2.y = 1000

p1 = GameImage('pillar4.png')
p1.x = 50
p1.y = 600

p2 = GameImage('pillar4.png')
p2.x = width - 100
p2.y = 600

fl1 = GameImage('flutuante1.png')
fl1.x = 250                            #entre o pilar da esquerda e a plataforma de cima
fl1.y = 600

fl2 = GameImage('flutuante1.png')
fl2.x = 1450                       
fl2.y = 600

objetos = [plat1, fl1, fl2, plat2, p1, p2]



