from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Web App with Python Flask!'


@app.route('/say_hey')
def hey_man():
    user = request.args.get('user')
    return f"Hey {user}!"


app.run(host='0.0.0.0')
