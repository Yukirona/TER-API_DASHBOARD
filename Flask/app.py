from flask import Flask, render_template
from api import init_POPT1, init_POPT0
import random

app = Flask(__name__)

df = init_POPT1()
df2 = init_POPT1()


@app.route('/')
def index():
        return render_template('index.html',)

@app.route('/home')
def first():
        return render_template('home.html')

@app.route('/Population')
def population():
        return render_template('population.html',  tables=[[df.to_html(table_id= 'POPT1')],[df2.to_html(table_id= 'POPT0')]])

