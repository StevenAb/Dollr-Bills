import os
from flask import Flask, request, render_template
from bill_type import * 
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html') 


@app.route('/upload', methods=['GET','POST'])
def upload():
    print(request.args)
    return render_template('index.html')
    #if request.method == 'POST':


@app.route('/results')
def results():
    balance = total()
    print balance
    return render_template('results.html', balance=balance)


def main():
    index()
