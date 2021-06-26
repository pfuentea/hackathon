from flask import Flask, render_template
from cartas import *
app = Flask(__name__)

red_belt_ninja= Unidad("Red Belt Ninja",3,3,4)
hard_algotithm=Hechizo("Hard Algorithm",2,"defensa",3)

objetos =[]
objetos.append(hard_algotithm)    


@app.route("/")
def hello_world():
    return render_template('index.html', objetos=objetos)


app.run(debug=True)
