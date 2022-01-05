from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from config2 import *

mapa1 = GameImage("plat1.png")
mapa1.x = 350
mapa1.y = 600

p1 = GameImage('pillar4.png')
p1.x = 50
p1.y = 600

p2 = GameImage('pillar4.png')
p2.x = width - 100
p2.y = 600

objetos = [mapa1, p1, p2]
obj_selected = []


