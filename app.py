from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
    name = {'username' : 'root'}
    rows = [
        {'name': 'Python', 'age': 27},
        {'name': 'Python', 'age': 27},
        {'name': 'Python', 'age': 27},
        {'name': 'Python', 'age': 27},
        {'name': 'Python', 'age': 27},
        {'name': 'Python', 'age': 27},
        {'name': 'Python', 'age': 27},
    ]
    return render_template('index.html', name=name, rows=rows)

if __name__ == "__main__":
    app.run(host='0.0.0.0')