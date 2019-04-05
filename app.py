# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 12:04:27 2019

@author: 1023180
"""
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/templates/')
@app.route('/templates/<name>')
def hello(name=None):
    return render_template('home.html', name=name)

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)