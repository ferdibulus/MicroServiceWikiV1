from www.TestApp.app import app
from flask import render_template
@app.route('/')
def home():
    return "Hello world!asddasda"


@app.route('/template')
def template():
    return render_template('home.html')