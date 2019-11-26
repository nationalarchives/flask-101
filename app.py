from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response('<h1>Have a cookie</h1>')
    response.set_cookie('hobnob', 'chocolate chip')
    return response