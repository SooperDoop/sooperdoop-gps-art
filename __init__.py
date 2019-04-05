# -*- coding: utf-8 -*-

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
#     return('hello')
    return render_template('index.html')

@app.route('/templates/')
@app.route('/templates/<name>')
def hello(name=None):
    return render_template('home.html', name=name)

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000)
