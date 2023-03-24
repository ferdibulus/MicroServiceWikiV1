from flask import Flask
app = Flask(__name__)

from flask import render_template
@app.route('/')
def home():
    return "Hello world!asddasda"


@app.route('/template')
def template():
    return render_template('home.html')