from flask import jsonify, request, url_for, g, current_app

from application.extensions import db, auth
from .. import api
from .model import User
from ..errors import bad_request
from datetime import datetime

@api.route('/users', methods=['POST'])
def register():
    """"""
    req = dict(request.get_json(force=True))
    user = User()
    user.from_dict(data=req, new_user=True)
    user.roles = 'operator'
    user.create()

    ret = {}

    ################################################################
    # Below, we will be defining the confirmation email that
    # users recieve after registering.
    ################################################################


    ret['token'] = auth.encode_jwt_token(user=user)
    ret['user'] = user.to_dict(include_email=True)

    return (jsonify(ret), 200)

@api.route('/confirm', methods=['POST'])
def confirm():
    """"""
    user = auth.get_user_from_registration_token(request.get_json(force=True)['token'])
    user.confirmed = True
    user.confirmed_on = datetime.now()

    ret = {
        'access_token': auth.encode_jwt_token(user)
    }
    return (jsonify(ret), 200)

@api.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    return jsonify(User.identify(id).to_dict())
