# Put your app in here.
from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route('/add')
def adds():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"<h1>a + b = {add(a, b)}</h1>"

@app.route('/sub')
def subtracting():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"<h1>a - b = {sub(a, b)}</h1>"

@app.route('/mult')
def multiplying():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"<h1>a * b = {mult(a, b)}</h1>"

@app.route('/div')
def dividing():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"<h1>a / b = {div(a, b)}</h1>"


# FURTHER STUDY 
# =========================================
OPERATIONS = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}

@app.route('/math/<view>')
def math_operations(view):
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = OPERATIONS[view](a, b)
    return f"The result of '{view}' operation is = {result}</h1>"
