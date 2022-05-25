from flask import Flask, render_template
from api import init_dash


app = Flask(__name__)

df = init_dash()


@app.route('/')
def index():
        return render_template('index.html',  tables=[df.to_html(classes='data')])
