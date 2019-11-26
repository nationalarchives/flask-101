from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<name>')
def user(name):
    return render_template('user.html', name=name)
