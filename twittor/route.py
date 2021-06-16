from flask import render_template
from twittor.forms import LoginForm

def index():
    name = {'username' : 'root'}
    postInput = [
        {
            "author": {"username": "Pan"},
            "body": "You can do it :)"
        },
        {
            "author": {"username": "test"},
            "body": "this is a test textAAA"
        },
        {
            "author": {"username": "test_b"},
            "body": "this is a test text_bAAA"
        }
    ]
    return render_template('index.html', name=name, postOutput=postInput)

def login():
    form = LoginForm(meta={'csrf': False})

    return render_template('login.html', title="Sign In", form=form)