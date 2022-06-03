from flask import Flask, render_template
from api import init_dash
import random

app = Flask(__name__)

df = init_dash()


@app.route('/Dashboard')
def index():
        return render_template('index.html')

@app.route('/Population')
def Population():
        return render_template('Pop.html',  tables=[df.to_html(classes='data')])

