from flask import jsonify, request, url_for, g, abort
from application.api import api

@api.route('/users/<int:id>', methods=['GET', 'POST'])
def get_user(id):
    if request.method == 'POST':

        data = request.get_json() or {}

        if 'email' not in data or 'password' not in data:
            return bad_request('Must provide email and password to register')
        if User.query.filter_by(email=data['email']):
            return bad_request('That email is already registered in our system. Please use a different one')

        user = User()
        user.from_dict(data, new_user=True)

        user.create()

        response = jsonify(user.to_dict())
        response.status_code = 201
        response.headers['Location'] = url_for('api.get_user', id=user.id)
        return response

    else:
        return jsonify(User.query.get_or_404(id).to_dict())


@api.route('/users', methods=['GET'])
def get_users():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = User.to_collection_dict(User.query, page, per_page, 'api.get_users')
    return jsonify(data)


@api.route('/users/<int:id>', methods=['POST'])
def update_user(id):
    if g.current_user.id != id:
        abort(403)

    user = User.query.get_or_404(id)
    data = request.get_json() or {}

    if 'email' in data and data['email'] != user.email and \
       User.query.filter_by(email=data['email']).first():
        pass # bad request

    user.from_dict(data, new_user=False)
    user.save()
    return jsonify(user.to_dict())
