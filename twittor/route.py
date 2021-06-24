from flask import render_template, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from twittor.forms import LoginForm, RegisterFrom
from twittor.models import User, Tweet
from twittor import db

@login_required
def index():
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
    return render_template('index.html', postOutput=postInput)

def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm(meta={'csrf': False})
    if form.validate_on_submit():
        u = User.query.filter_by(username=form.username.data).first()
        if u is None or not u.check_password(form.password.data):
            print('invalid username or password')
            return redirect(url_for('login'))
        login_user(u, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if next_page:
            return redirect(next_page)
        return redirect(url_for('index'))
    return render_template('login.html', title="Sign In", form=form)

def logout():
    logout_user()
    return redirect(url_for('login'))

def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterFrom()
    if form.validate_on_submit():
        user = User(username=form.username.data, email = form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title='Registration', form=form)

