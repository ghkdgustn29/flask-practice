from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Hello, Hello!'

@app.route('/bone')
def hello_bone():
    return 'idiot!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
