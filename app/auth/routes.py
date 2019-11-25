from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from sqlalchemy.exc import IntegrityError

from app import db
from app.api.models import User
from app.auth import bp
from app.auth.forms import LoginForm, RegistrationForm
from app.email import send_confirmation_email

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
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
        return redirect(url_for(main.index))

    form = RegistrationForm()

    if request.method == 'POST':
        try:
            user = User(first=request.form['first'],
                        last=request.form['last'],
                        email=request.form['email'])

            user.set_password(request.form['password'])
            db.session.add(user)
            db.session.commit()

            # TODO: add email confirmation
            send_confirmation_email(user.email)
            flash('User registered! Please check your email, you should get a confirmation message within 5 minutes!')
            # TODO: New Set Up Profile module
            return redirect(url_for('main.index', nav=True))
        except IntegrityError:
            db.session.rollback()
            flash('Email address is already in our system. Please choose a different one.', 'danger')
            return redirect(url_for('auth.register'))
    return render_template('register.html', title='Register',form=form, nav=True)

@bp.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    # TODO: Password reset
    # if current_user.is_authenticated:
    #     return redirect(url_for('main.index'))
    pass

@bp.route('/confirm/<token>')
def confirm_email(token):
    try:
        confirm_serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
        email = confirm_serializer.loads(token, salt='email-confirmation-salt', max_age=3600)
    except:
        flash('The confirmation link is no longer valid.', 'danger')
        return redirect(url_for('auth.login'))

    user = User.query.filter_by(email=email).first()

    if user.confirmed:
        flash('Account already confirmed. Please log in.')
    else:
        user.confirmed = True
        user.confirmed_on = datetime.now()
        db.session.add(user)
        db.session.commit()
        flash('Email has been confirmed!', 'success')

    # TODO: create profile (demographics redirect)
    return redirect(url_for('main.index'))
