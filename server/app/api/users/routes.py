from flask import jsonify, request, url_for, g, current_app, render_template
from flask_cors import cross_origin
from app.extensions import db, auth
from config import Config
from .. import api
from .model import User
from ..errors import bad_request
from datetime import datetime

CLIENT_URL = Config.CLIENT_URL

@api.route('/users', methods=['POST'])
@cross_origin(origin='localhost', headers=['Content-Type', 'access-control-allow-origin'])
def register():
    """
    Creates a new user and sends registration email
    :returns: jsonified message, and user information
    """
    req = dict(request.get_json(force=True))
    user = User()
    user.from_dict(data=req, new_user=True)
    user.create()

    ################################################################
    # Below, we will be defining the confirmation email that
    # users receive after registering.
    ################################################################

    auth.send_registration_email(email=user.email,
                                  user=user,
                                  template= render_template('registration_email.html'),
                                  confirmation_uri=CLIENT_URL + '/ confirm')

    ################################################################
    # Defining the server response to successful register request
    ################################################################
    res = {
        'message': 'Registration email sent to {0}.'.format(user.email) + \
                   'Please check your email to confirm your account',
        'user': user.to_dict(include_email=True)
    }

    return jsonify(res), 200


@api.route('/confirm', methods=['POST'])
@cross_origin(origin='localhost', headers=['Content-Type', 'access-control-allow-origin', 'Authorization'])
def confirm():
    """
    Confirms the user using the registration link sent to the users inbox

    :returns: newly generated access token
    """
    token = auth.read_token_from_header()
    user = auth.get_user_from_registration_token(token)

    user.confirmed = True
    user.confirmed_on = datetime.now()

    ret = {
        'access_token': auth.encode_jwt_token(user)
    }
    return jsonify(ret), 200


@api.route('/users/<int:id>', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content-Type', 'access-control-allow-origin', 'Authorization'])
def get_user(id):
    """
    Returns the user associated with the given ID

    :param id: unique UID of the given users
    :returns: jsonified user information
    """
    return jsonify(User.identify(id).to_dict())
