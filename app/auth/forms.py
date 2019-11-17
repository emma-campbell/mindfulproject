from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from app.api.models import User

class LoginForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):

    first = StringField('First', validators=[DataRequired()])
    last = StringField('Last', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(),
                                                              EqualTo('password')])
    submit = SubmitField('Register')

    def validate_email(self, email):
        user.User.query.filter_by(email=email).first()
        if user is not None:
            raise ValidationError("That email is already in our system. Please use a different one.")
