import wtforms
from models import UserModel
from wtforms.validators import Length, Email, NumberRange, Optional
from exts import db


class RegisterForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email()])
    firstname = wtforms.StringField(validators=[Length(min=1, max=20, message="Firstname needs to be no more than 20 letters.")])
    lastname = wtforms.StringField(validators=[Length(min=1, max=20, message="Lastname needs to be no more than 20 letters.")])
    password = wtforms.StringField(validators=[Length(min=1, max=20, message="Password needs to be no more than 20 letters.")])

    def validate_email(self, field):
        email = field.data
        user = db.session.execute(db.select(UserModel).filter_by(email=email)).scalar()
        if user:
            raise wtforms.ValidationError(message="This email was registed!")


class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email()])
    password = wtforms.StringField(validators=[Length(min=1, max=20, message="Password needs to be no more than 20 letters.")])


class TargetForm(wtforms.Form):
    targetleetcode = wtforms.IntegerField(validators=[Optional(), NumberRange(1,9999)])
    targetproject = wtforms.IntegerField(validators=[Optional(), NumberRange(1,10)])
    targetdate = wtforms.DateField(validators=[Optional()], format='%Y-%m-%d')
    startdate = wtforms.DateField(validators=[Optional()], format='%Y-%m-%d')

class CurrentForm(wtforms.Form):
    currentleetcode = wtforms.IntegerField(validators=[Optional(), NumberRange(1,9999)])
    currentproject = wtforms.IntegerField(validators=[Optional(), NumberRange(1,10)])
    currentinterview = wtforms.IntegerField(validators=[Optional(), NumberRange(1,10)])
    resume = wtforms.BooleanField(validators=[Optional()])
    bq = wtforms.BooleanField(validators=[Optional()])
    tq = wtforms.BooleanField(validators=[Optional()])
    mock = wtforms.BooleanField(validators=[Optional()])