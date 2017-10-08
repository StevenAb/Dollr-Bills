import os
from flask import Flask, request, render_template
app = Flask(__name__)
balance = 0

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        #login or some shit
        pass
    else:
        #don't do that
        pass

@app.route('/users/<username>')
def profile(username=None):
    return render_template('user.html', name=username)

@app.route('/upload', methods=['GET','POST'])
def upload():
    print(request.args)
    return render_template('index.html')
    #if request.method == 'POST':
        
