from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>This is a Heading</h1>
<p>This is a paragraph.</p>

</body>
</html>
"""

@app.route('/test')
def test():
    return "this is a test"