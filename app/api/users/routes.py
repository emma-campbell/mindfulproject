from flask import jsonify, request, url_for, g, abort, render_template, redirect
from flask_login import login_user, logout_user, current_user
from app import db, login
from sqlalchemy import desc

from . import User
from app.api import bp
from app.api.auth import token_auth
from app.api.errors import bad_request
from app.api.journal import Journal
from app.main.forms import JournalForm


@bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    return jsonify(User.query.get_or_404(id).to_dict())

@bp.route('/users', methods=['GET'])
def get_users():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = User.to_collection_dict(User.query, page, per_page, 'api.get_users')
    return jsonify(data)

@bp.route('/users', methods=['POST'])
def create_user():

    data = request.get_json() or {}

    # TODO: Check that ALL required fields are in the request
    # if they aren't, it's a bad request.
    if 'email' not in data or 'password' not in data:
        return bad_request('must include username, email, and password fields')
    if User.query.filter_by(email=data['email']):
        return bad_request('please use a different email')


    user = User()
    user.from_dict(data, new_user=True)

    db.session.add(user)
    db.session.commit()

    response = jsonify(user.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('api.get_user', id=user.id)
    return response

@bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):

    if g.current_user.id != id:
        abort(403)

    user = User.query.get_or_404(id)
    data = request.get_json() or {}

    if 'email' in data and data['email'] != user.email and \
       User.query.filter_by(email=data['email']).first():
        pass # bad request
    user.from_dict(data, new_user=False)
    db.session.commit()
    return jsonify(user.to_dict())

@bp.route('/journals', methods=['GET', 'POST'])
def journals():
    if current_user.is_authenticated:
        user_journals = Journal.query.filter_by(user_id=current_user.id).all()
        user_journals.reverse
        first = []
        second = []
        third = []
        for journal in user_journals:
            if user_journals.index(journal) % 3 == 0:
                first.append(journal)
            if user_journals.index(journal) % 3 == 1:
                second.append(journal)
            if user_journals.index(journal) % 3 == 2:
                third.append(journal)
        return render_template('journals.html', nav=True, user=current_user, first=first, second=second, third=third)
    else:
        return redirect(url_for('main.index'))

@bp.route('/journal_edit/<int:entry_id>', methods=['GET', 'POST'])
@bp.route('/journal_edit', methods=['GET', 'POST'])
def journal_edit(entry_id=None):
    if entry_id is None:
        form = JournalForm()
        if form.validate_on_submit():
            # The user pressed the "Save" button
            if form.save.data:
                j = Journal(title=request.form['title'],
                            user=current_user,
                            entry=request.form['entry'])
                db.session.add(j)
                db.session.commit()
                return redirect(url_for('.journals'))
            # else The user pressed the "Cancel" button
            else:
                return redirect(url_for('.journals'))
    else:
        j = Journal.query.filter_by(id=entry_id).first()
        form = JournalForm()
        if request.method == 'GET':
            print("HERE")
            form.title.data = j.title
            form.entry.data = j.entry
        else:
            if form.save.data:
                if form.title.data:
                    j.title = form.title.data
                if form.entry.data:
                    j.entry = form.entry.data
                db.session.commit()
                return redirect(url_for('.journals'))
            # else The user pressed the "Cancel" button
            else:
                return redirect(url_for('.journals'))
    return render_template('journal-edit.html', nav=True, form=form)


@bp.route('/journal_delete/<int:entry_id>', methods=['GET', 'POST'])
def journal_delete(entry_id):
    j = Journal.query.filter_by(id=entry_id).first()
    db.session.delete(j)
    db.session.commit()
    return redirect(url_for('.journals'))

