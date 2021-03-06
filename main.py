import os

from flask import Flask
app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello world!'

@app.route('/hello_name/<name>')
def hello_name(name):
    return 'Hello {}!'.format(name)

@app.route('/')
def home():
    return 'Welcome home!'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
