from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
<!doctype html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
  body { text-align: center; }

  p { color: gray; }
  </style>
</head>
<body>
  <h1 onclick="hi()">Hello, world!</h1>
  <hr>
  <p>안녕!</p>

<script>
function hi() {
  document.querySelector('body > p').innerHTML += " 안녕!";
}
</script>
</body>
</html>
"""

@app.route('/bone')
def hello_bone():
    return 'idiot!'

@app.route('/bone/<name>')
def hello_name(name):
    return name

if __name__ == '__main__':
    app.run(host='0.0.0.0')
