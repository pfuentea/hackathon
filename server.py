from flask import Flask, render_template
from baraja import *
app = Flask(__name__)

objetos=[]
app.cont=0
cartas_por_mostrar=[]

@app.route("/")
def hello_world():
    if app.cont < len(baraja):
        objetos.append(baraja[app.cont])
        app.cont+=1
    return render_template('index.html', objetos=objetos)


app.run(debug=True)
