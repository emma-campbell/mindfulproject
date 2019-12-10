from flask import jsonify, g

from .. import api
from ..users.model import User

from . import basic_auth, token_auth

@api.route('/tokens', methods=['POST'])
@basic_auth.login_required
def get_token():
    token = g.current_user.get_token()
    g.current_user.save()
    return jsonify({'token' : token })


@api.route('/tokens', methods=['DELETE'])
@token_auth.login_required
def revoke_token():
    g.current_user.revoke_token()
    g.current_user.save()
    return'', 204

@basic_auth.verify_password
def verify_password(email_or_token, password):
    user = User.check_token(email_or_token)
    if not user:
        user = User.query.filter_by(email=email_or_token).first()
        if not user or not user.check_password(password):
            return False

    g.user = user
    return True
