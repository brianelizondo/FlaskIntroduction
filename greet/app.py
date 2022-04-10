from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return "welcome"

@app.route('/welcome/<folder>')
def welcome_folder(folder):
    return f"welcome {folder}"

