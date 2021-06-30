from cartas import *

criaturas=[]
criaturas.append(Unidad("Red Belt Ninja",3,3,4,"vader.PNG"))
criaturas.append(Unidad("Black Belt Ninja ",4,5,4,"vader.PNG"))
criaturas.append(Unidad("Lag Man ",3,3,2,"vader.PNG"))

spells=[]
spells.append(Hechizo("Hard Algorithm",2,"defensa",3,""))
spells.append(Hechizo("Promesa no manejada",1,"defensa",-2,""))
spells.append(Hechizo("Pair Programing",3,"ataque",2,""))

coleccion=criaturas+spells


baraja=coleccion


