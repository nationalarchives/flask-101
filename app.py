from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Life is short, buy the guitar'