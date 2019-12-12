from flask import jsonify, request, url_for, g, current_app

from application.extensions import db, auth
from .. import api
from .model import User
from ..errors import bad_request
from datetime import datetime

@api.route('/users', methods=['POST'])
def register():
    """"""
    req = request.get_json(force=True)

    name = req.get('name', None)
    email = req.get('email', None)
    password = req.get('password', None)

    user = User(
        name=name,
        email=email,
        password=auth.hash_password(password),
        roles='operator'
    )

    user.create()
    ret = {}

    ################################################################
    # Below, we will be defining the confirmation email that
    # users recieve after registering.
    #
    #     - Generate the URL
    ################################################################

    uri = url_for('api.confirm', _external=True)

    ret['token'] = auth.send_registration_email(email, user=user, confirmation_uri=uri)['token']

    return (jsonify(ret), 200)

@api.route('/confirm/', methods=['POST'])
def confirm():
    """"""
    user = auth.get_user_from_registration_token(request.args.get('token'))
    user.confirmed = True
    user.confirmed_on = datetime.now()

    ret = {
        'access_token': auth.encode_jwt_token(user)
    }
    return (jsonify(ret), 200)
