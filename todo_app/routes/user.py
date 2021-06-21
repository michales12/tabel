from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user, current_user, logout_user
from todo_app.extensions import db
from todo_app.forms import RegistrationForm, LoginForm
from todo_app.models import User

user=Blueprint("user",__name__)

@user.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user.login'))
    return render_template('Register.html', title='Register', form=form)

@user.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('index'))
    return render_template('SignIn.html', title='SignIn', form=form)

@user.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))