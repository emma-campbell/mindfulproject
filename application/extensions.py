from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

from flask_sqlalchemy.model import DefaultMeta, Model
from sqlalchemy.ext.declarative import declarative_base, declared_attr

import flask_praetorian
import logging

db = SQLAlchemy(model_class=Model)
mail = Mail()
auth = flask_praetorian.Praetorian()
logger = logging.getLogger()
