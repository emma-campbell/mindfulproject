from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, FileField, TextAreaField, DateField, SelectField
from wtforms.validators import DataRequired, ValidationError, Email, Regexp

from app.api.users import User
from app import db

class UploadImage(FlaskForm):

    img = FileField('Image File', validators=[Regexp(u'^[^/\\\\]\.jpg$')])
    upload = SubmitField('Upload')

    def validate_image(form, field):
        if field.data:
            field.data = re.sub(r'[^a-z0-9_.-]', '_', field.data)

def upload(request):
    form = UploadForm(request.POST)
    if form.image.data:
        image_data = request.FILES[form.image.name].read()
        open(os.path.join(UPLOAD_PATH, form.image_data), 'w').write(image_data)

class Demographics(FlaskForm):

    bday = DateField('Date of Birth')
    race = SelectField('Race', choices=['White', 'Black/African American', 'Hispanic or Latino American', 'Asian American', 'Native Hawaiian/Pacific Islander', 'Two or more races', 'Other', 'Do not wish to disclose'])
    gender = SelectField('Gender', choices=['Male', 'Female', 'Other', 'Do not wish to disclose'])
    orientation = SelectField('Sexual Orientation', choices=['Straight', 'Gay', 'Lesbian', 'Bisexual', 'Other', 'N/A or do not wish to disclose'])

    condition = SelectField('Have you been diagnosed with a psychiatric illness?', choices=['Yes', 'No'])

class JournalForm(FlaskForm):

    title = StringField('Title', validators=[DataRequired()])
    entry = TextAreaField('Entry', validators=[DataRequired()])
    save = SubmitField('Save')
    cancel = SubmitField('Cancel')
