from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, \
    jsonify, current_app
from flask_login import current_user, login_required

from app import db, login
from app.api.users import User
from app.main import bp

@bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', nav=True)

@bp.route('/unconfirmed')
@login_required
def unconfirmed():
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('unconfirmed.html')