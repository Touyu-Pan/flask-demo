from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Twittor</title>
</head>
<body>
    <h1>Hello, Twittor</h1> 
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host='0.0.0.0')