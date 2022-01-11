from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from config2 import *

#mapa

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

p3 = GameImage('Pillar1.png')
p3.x = 200
p3.y = 700

p4 = GameImage('Pillar1.png')
p4.x = 400
p4.y = 800

p5 = GameImage('Pillar1.png')
p5.x = 1450
p5.y = 800

p6 = GameImage('Pillar1.png')
p6.x = 1650
p6.y = 700

selected_obj = []
selected_obj2 = []
objetos = [plat1, plat2, p1, p2, p3, p4, p5, p6]

#power-ups

pw_atk = GameImage('pw1.png')
pw_hp = GameImage('pw2.png')

pw_list = [pw_atk, pw_hp]
pw_coords = [[plat1.x, plat1.y],[plat2.x, plat2.y],[p1.x, p1.y],[p2.x, p2.y],[p3.x, p3.y],[p4.x, p4.y],[width/2, p1.y],[width/2, p2.y]]
pw_spawned = []
pw_collected = []
pw_collected2 = []



