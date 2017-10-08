import os
from flask import Flask, request, render_template
from bill_type import * 
from get_stock_ import *
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
    stock = getStock(balance)
    price = stock[0]
    name = stock[1]
    return render_template('results.html', balance=balance, price=price, name=name)


def main():
    index()
