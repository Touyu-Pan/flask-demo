from flask import render_template, redirect, url_for
from twittor.forms import LoginForm
from twittor.models import User

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
    if form.validate_on_submit():
        msg = "username={}, password={}, remember_me={}".format(
            form.username.data,
            form.password.data,
            form.remember_me.data
        )
        print(msg)
        return redirect(url_for('index'))
    return render_template('login.html', title="Sign In", form=form)