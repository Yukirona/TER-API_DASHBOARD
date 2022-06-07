from flask import Flask, render_template
from api import init_dash
import random

app = Flask(__name__)

df = init_dash()


@app.route('/')
def index():
        return render_template('index.html')

@app.route('/first')
def first():
        return render_template('first.html')

@app.route('/Population')
def population():
        return render_template('population.html',  tables=[df.to_html(classes='data')])

