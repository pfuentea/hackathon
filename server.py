from flask import Flask, render_template

app = Flask(__name__)


objetos = [
    {
        'nombre': 'Pepe',
        'edad': 34
    },
    {
        'nombre': 'Juana',
        'edad': 23
    },
    {
        'nombre': 'Julia',
        'edad': 12
    }
]

@app.route("/")
def hello_world():
    return render_template('index.html', objetos=objetos)


app.run()