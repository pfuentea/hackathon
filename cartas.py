class Card:
    def __init__(self,nombre,coste):
        self.nombre=nombre
        self.costo=coste

    def CardToJson(self):
        if isinstance(self, Unidad) == True :
            json="{'nombre':"+self.nombre +",'costo':"+str(self.costo)+"}"
            print("Unidad")

        else:
            json="{'nombre':'"+self.nombre +"','costo':"+str(self.costo)+" ,'stat':'"+self.stat+"' }"
            print("Hechizo")
            return json

class Hechizo(Card):
    def __init__(self,nombre,coste,stat,magnitud):
        super().__init__(nombre,coste)
        self.stat=stat
        self.magnitud=magnitud
    
    def lanzar(self,Objetivo):
        #identificar si es una unidad
        # if target instance Unit:
        if isinstance(Objetivo, Unidad) == True :
            if self.stat=="attack" :
                Objetivo.attack+= self.magnitud
            if self.stat=="defense" :
                Objetivo.defense+= self.magnitud
        else:
            print( "Target must be a unit!")    

    

class Unidad(Card):
    def __init__(self,nombre,coste,ataque,defensa):
        super().__init__(nombre,coste)
        self.attack=ataque
        self.defense=defensa

    def atacar(self,Objetivo):
        pass



