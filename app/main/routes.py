from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, \
    jsonify, current_app
from flask_login import current_user, login_required

from app import db, login
from app.models import User
from app.main import bp

@bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main/index.html')

@bp.route('/user/<id>', methods=['GET', 'POST'])
def user(id):
    user = User.query.filter_by(id=int(id)).first_404()

    print(user)
    print(user.access)
    return render_template('user.html', user=user)
