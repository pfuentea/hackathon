from _typeshed import StrPath


class Card:
    def __init__(self,nombre,coste):
        self.nombre=nombre
        self.costo=coste

class Hechizo(Card):
    def __init__(self,nombre,coste,stat,magnitud):
        super(nombre,coste)
        self.stat=stat
        self.magnitud=magnitud
    
    def lanzar(self,Objetivo):
        if self.stat=="attack" :
            Objetivo.attack+= self.magnitud
        if self.stat=="defense" :
            Objetivo.defense+= self.magnitud
            

class Unidad(Card):
    def __init__(self):
        self.atttack=0
        self.defense=0

    def ver_carta(self):
        print("")
        print(f"|{self.nombre}|")
        print("------------------")
        print(f"|{self.costo}|")

