import re
from flask import render_template, redirect, url_for, request, abort
from flask_login import login_user, current_user, logout_user, login_required
from twittor.forms import LoginForm, RegisterFrom, EditProfileForm, TweetForm
from twittor.models import User, Tweet
from twittor import db

@login_required
def index():
    form = TweetForm()
    if form.validate_on_submit():
        t = Tweet(body=form.tweet.data, author=current_user)
        if form.btn_cancel.data:
            return redirect(url_for('index', username = current_user.username))
        db.session.add(t)
        db.session.commit()
        return redirect(url_for('index'))
    tweets = current_user.own_and_followed_tweets()
    return render_template('index.html', tweets=tweets, form=form)

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

@login_required
def user(username):
    u = User.query.filter_by(username=username).first()
    if u is None:
        abort(404)

    tweets = u.tweets.order_by(Tweet.create_time.desc())
    
    if request.method == 'POST':
        if request.form['request_button'] == 'Follow':
            current_user.follow(u)
            db.session.commit()
        else:
            current_user.unfollow(u)
            db.session.commit()
    return render_template('user.html', title='Profile', tweets=tweets, user=u)

def page_not_found(e):
    return render_template('404.html'), 404

@login_required
def edit_profile():
    form = EditProfileForm()
    if request.method == 'GET':
        form.about_me.data = current_user.about_me
    if form.validate_on_submit():
        if form.btn_cancel.data:
            return redirect(url_for('profile', username = current_user.username))
        current_user.about_me = form.about_me.data
        db.session.commit()
        return redirect(url_for('profile', username = current_user.username))
    return render_template('edit_profile.html', title='Profile Editer', form=form)
