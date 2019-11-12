from flask import jsonify, request, url_for, g, abort
from app import db

from app.models import User
from app.api import bp
# from app.api.auth import token_auth
# from app.api.errors import bad_request

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
        # Bad Request
        pass

    if User.query.filter_by(email=data['email']):
        # Bad Request
        pass


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
