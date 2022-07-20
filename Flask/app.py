from flask import Flask, render_template
from api import init_POPT1, init_FAMG1, init_FAMG5
import random

app = Flask(__name__)

df = init_FAMG1()
df2 = init_POPT1()
df3 = init_FAMG5()


@app.route('/')
def index():
        return render_template('index.html',)

@app.route('/chart')
def chart():
        return render_template('chart.html',)

@app.route('/home')
def first():
        return render_template('home.html')

@app.route('/Population')
def population():
        return render_template('population.html',  tables=[[df],[df2],[df3]])

