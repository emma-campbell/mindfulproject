from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from sqlalchemy.exc import IntegrityError
from datetime import datetime

from app import db
from app.api.users import User
from app.api.tokens import confirm_token
from app.auth import bp
from app.auth.forms import LoginForm, RegistrationForm, ResetPasswordRequestForm, ResetPasswordForm
from app.email import send_confirmation_email, send_password_reset_email

from config import Config

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for(main.index))
    form = LoginForm()
    if request.method == "POST":
        user = User.query.filter_by(email=request.form['email']).first()

        if user is None or not user.check_password(request.form['password']):
            flash('Invalid email or password.', 'danger')
            return redirect(url_for('.login'))

        login_user(user)

        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)
    return render_template('login.html', title='Welcome Back!', form=form, nav=True)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@bp.route('/register', methods=['GET', 'POST'])
def register():
    """Register a new user"""
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = RegistrationForm()

    if request.method == 'POST':
        try:
            user = User(first=request.form['first'],
                        last=request.form['last'],
                        email=request.form['email'])

            user.set_password(request.form['password'])

            db.session.add(user)
            db.session.commit()

            send_confirmation_email(user.email)
            flash('User registered! Please check your email, you should get a ' +
                  'confirmation message within 5 minutes!')

            # TODO: New Set Up Profile module
            return redirect(url_for('main.unconfirmed', nav=True))

        except IntegrityError:
            db.session.rollback()
            flash('Email address is already in our system. Please choose a different one.', 'danger')
            return redirect(url_for('auth.register'))
    return render_template('register.html', title='Register',form=form, nav=True)

@bp.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=request.form['email']).first()
        if user is None:
            flash('Email not found.', 'danger')
            return redirect(url_for('.reset_password_request'))

        send_password_reset_email(user)
        flash('Check your email for instructions to reset your password.')
        return redirect(url_for('.login'))
    return render_template('reset_password_request.html',
                           title='Reset Password', form=form)


@bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    user = User.verify_reset_password_token(token)
    if not user:
        print("Second")
        return redirect(url_for('main.index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(request.form['password'])
        db.session.commit()
        flash('Your password has been reset!', 'success')
        return redirect(url_for('.login'))
    return render_template('reset_password.html', form=form)

@bp.route('/confirm/<token>')
def confirm_email(token):
    try:
        email = confirm_token(token)
    except:
        flash('The confirmation link is no longer valid.', 'danger')
        return redirect(url_for('auth.login'))

    user = User.query.filter_by(email=email).first()

    if user is not None:
        if user.confirmed == True:
            flash('Account already confirmed. Please log in.')
        else:
            user.confirmed = True
            user.confirmed_on = datetime.now()
            db.session.add(user)
            db.session.commit()
            flash('Email has been confirmed!', 'success')

    # TODO: create profile (demographics redirect)
    return redirect(url_for('main.index'))
