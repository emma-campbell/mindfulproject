from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user

from app import db
from app.models import User
from app.auth import bp
from app.auth.forms import LoginForm, RegistrationForm

@bp.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for(main.index))

    form = LoginForm()

    if request.method == "POST":

        user = User.query.filter_by(email=request.form['email']).first()
        print (user)
        if user is None or not user.check_password(request.form['password']):
            flash('Invalid email or password.')
            return redirect(url_for('auth.login'))


        login_user(user)
        print(user)

        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)
    return render_template('auth/login.html', title='Welcome Back!', form=form, nav=True)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect('main.index')

@bp.route('/register', methods=['GET', 'POST'])
def register():

    if current_user.is_authenticated:
        return redirect(url_for(main.index))

    form = RegistrationForm()

    if request.method == 'POST':

        user = User(first=request.form['first'],
                    last=request.form['last'],
                    email=request.form['email'])

        user.set_password(request.form['password'])

        db.session.add(user)
        db.session.commit()

        flash('User {0} has been registered!'.format(user.id))
        return redirect(url_for('main.index', nav=True))

    return render_template('auth/register.html',
                           title='Register',
                           form=form,
                           nav=True)
