from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email


class Login(FlaskForm):
    email =  StringField('Email', validators = [InputRequired(), Email()])
    password = PasswordField('Password', validators = [InputRequired()])
    sumbit = SubmitField('Sign in')


class Register(FlaskForm):
    first_name = StringField("First Name", validators = [InputRequired()])
    last_name = StringField("Last Name", validators = [InputRequired()])
    email = StringField('Email', validators = [InputRequired(), Email()])
    password = PasswordField('Password', validators = [InputRequired()])
    submit = SubmitField('Register')


        




