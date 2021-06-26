from flask import Flask, render_template
from baraja import *
app = Flask(__name__)



objetos =baraja


@app.route("/")
def hello_world():
    return render_template('index.html', objetos=objetos)


app.run(debug=True)
