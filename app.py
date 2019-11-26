from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Life is short, buy the guitar'

@app.route('/<param>')
def thing(param):
    return 'Life is short, buy the {}'.format(param)
