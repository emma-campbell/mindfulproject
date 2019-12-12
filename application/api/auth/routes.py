from flask import render_template, redirect, url_for, flash, request, jsonify
from sqlalchemy.exc import IntegrityError
from datetime import datetime

from application.extensions import auth

from .. import api
from ..users.model import User

from ..errors import bad_request

from config import Config

@api.route('/login', methods=['POST'])
def login():
   """"""
   req = request.get_json(force=True)
   email = req.get('email', None)
   password = req.get('password', None)
   user = auth.authenticate(email, password)
   ret = {
      'access_token' : auth.encode_jwt_token(user)
   }
   return jsonify(ret), 200
