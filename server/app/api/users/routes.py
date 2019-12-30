from flask import jsonify, request, url_for, g, current_app

from app.extensions import db, auth
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

    ################################################################
    # Below, we will be defining the confirmation email that
    # users receive after registering.
    ################################################################

    ret = {'token': auth.send_registration_email(email=user.email, user=user)['token'], 'user': user.to_dict(include_email=True)}
    return jsonify(ret), 200


@api.route('/confirm', methods=['POST'])
def confirm():
    """"""
    logger = current_app.logger
    token = auth.read_token_from_header()
    user = auth.get_user_from_registration_token(token)

    user.confirmed = True
    user.confirmed_on = datetime.now()

    ret = {
        'access_token': auth.encode_jwt_token(user)
    }
    return jsonify(ret), 200


@api.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    return jsonify(User.identify(id).to_dict())
