class Card:
    def __init__(self,nombre,coste,tipo,imagen):
        self.nombre=nombre
        self.costo=coste
        self.tipo=tipo
        self.imagen=imagen

class Hechizo(Card):
    def __init__(self,nombre,coste,stat,magnitud):
        super().__init__(nombre,coste,'hechizo')
        self.stat=stat
        self.magnitud=magnitud
    
    def lanzar(self,Objetivo):
        #identificar si es una unidad
        # if target instance Unit:
        if isinstance(Objetivo, Unidad) == True :
            if self.stat=="ataque" :
                Objetivo.attack+= self.magnitud
            if self.stat=="defensa" :
                Objetivo.defense+= self.magnitud
        else:
            print( "Target must be a unit!")    

class Unidad(Card):
    def __init__(self,nombre,coste,ataque,defensa):
        super().__init__(nombre,coste,'unidad')
        self.attack=ataque
        self.defense=defensa

    def atacar(self,Objetivo):
        Objetivo.defense -=self.attack
        