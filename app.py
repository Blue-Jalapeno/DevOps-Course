# DevOps Project - ThinkNyx

from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return "Hello and welcome to the ThinkNyx DevOps project!"

@app.route('/services')
def services():
    return "Here are our services!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)