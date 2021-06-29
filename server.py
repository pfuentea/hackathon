from flask import Flask, render_template
from baraja import *
app = Flask(__name__)

objetos=[]
app.cont=0

cartas_por_mostrar=[]

def jugada1():
    cartas_por_mostrar.append(criaturas[0])


def jugada2():
    cartas_por_mostrar.clear()
    h1=spells[0]
    c1=criaturas[0]
    #print(f"Carta:{c1.nombre},ATK:{c1.attack} DEF: {c1.defense}")  
    cartas_por_mostrar.append(h1)
    h1.lanzar(c1) 
    cartas_por_mostrar.append(c1)
    #print(f"Carta:{c1.nombre},ATK:{c1.attack} DEF: {c1.defense}")  

def jugada3():
    cartas_por_mostrar.clear()
    c1=criaturas[0]
    c2=criaturas[1]
    cartas_por_mostrar.append(c1)
    cartas_por_mostrar.append(c2)


def jugada4():
    cartas_por_mostrar.clear()
    c1=criaturas[0]
    h1=spells[1]
    h1.lanzar(c1) 
    cartas_por_mostrar.append(h1)
    cartas_por_mostrar.append(c1)

def jugada5():
    cartas_por_mostrar.clear()
    c1=criaturas[0]
    h1=spells[2]
    h1.lanzar(c1) 
    cartas_por_mostrar.append(h1)
    cartas_por_mostrar.append(c1)

def jugada6():
    cartas_por_mostrar.clear()
    c1=criaturas[0]
    c2=criaturas[1]
    c1.atacar(c2)
    cartas_por_mostrar.append(c1)
    cartas_por_mostrar.append(c2)

jugadas=[jugada1,jugada2,jugada3,jugada4,jugada5,jugada6]

app.sgte_jugada=0 


@app.route("/")
def hello_world():
    #if app.cont < len(baraja):
        #objetos.append(baraja[app.cont])
        #app.cont+=1

    #revisar que no me pase de jugadas
    if app.sgte_jugada < len(jugadas):
        jugadas[app.sgte_jugada]()
        app.sgte_jugada +=1
        boton="on"
        if app.sgte_jugada == len(jugadas):
            boton="off"
        return render_template('index.html', objetos=cartas_por_mostrar,boton=boton)

app.run(debug=True)