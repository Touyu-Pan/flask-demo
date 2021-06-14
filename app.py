from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
    name = {'username' : 'root'}
    postInput = [
        {
            "author": {"username": "Pan"},
            "body": "You can do it :)"
        },
        {
            "author": {"username": "test"},
            "body": "this is a test textAAA"
        }
    ]
    return render_template('index.html', name=name, postOutput=postInput)

if __name__ == "__main__":
    app.run(host='0.0.0.0')