from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

#lojas

loja1 = GameImage('Vendedor.png')
loja1.set_position(500, 460)

loja2 = GameImage('Vendedor.png')
loja2.set_position(1300, 460)

#top left

r1 = GameImage("Blue_Row.png")
r1.set_position(50,0)

r2 = GameImage("Blue_Row.png")
r2.set_position(440,0)

r3 = GameImage("Blue_Row.png")
r3.set_position(0,430)

r4 = GameImage("Blue_Row.png")
r4.set_position(490,430)

c1 = GameImage("Blue_Col.png")
c1.set_position(0,0)

c2 = GameImage("Blue_Col.png")
c2.set_position(825,0)



#bottom left

r5 = GameImage("Blue_Row.png")
r5.set_position(0,530)

r6 = GameImage("Blue_Row.png")
r6.set_position(490,530)

r7 = GameImage("Blue_Row.png")
r7.set_position(60,985)

r8 = GameImage("Blue_Row.png")
r8.set_position(440,985)

c3 = GameImage("Blue_Col.png")                     
c3.set_position(0, 600)

c4 = GameImage("Blue_Col.png")
c4.set_position(825, 600)

ca1 = GameImage("Casa.png")
ca1.set_position(175, 600)

ca2 = GameImage("Casa.png")
ca2.set_position(650, 600)

ce1 = GameImage("Cerca.png")
ce1.set_position(50, 600)

ce2 = GameImage("Cerca.png")
ce2.set_position(300, 600)



objects = [c1, c2, c3, c4, r1, r2, r3, r4, r5, r6, r7, r8, ca1, ca2, ce1, ce2]
obj_selected = []
