from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField, validators, PasswordField, HiddenField, BooleanField, IntegerField, FormField
from connect_mongodb import col_user

class SignupForm(FlaskForm):
    username = TextField('Username',  [
        validators.Required('Please enter your username.'),
        validators.Length(max=30, message='Username is at most 30 characters.'),
    ])
    email = TextField('Email',  [
        validators.Required('Please enter your email address.'),
        validators.Email('Please enter your email address.')
    ])
    password = PasswordField('Password', [
        validators.Required('Please enter a password.'),
        validators.Length(min=6, message='Passwords is at least 6 characters.'),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Create account')

    def __init__(self, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)

    def validate(self):
        if not FlaskForm.validate(self):
            return False

        username = col_user.find({"username":self.username.data})
        if username:
            self.username.errors.append('That username is already taken.')
            return False
        user_email = col_user.find({"email":self.email.data})
        if user_email:
            self.username.errors.append('That email is already taken.')
            return False

        return True
    



class LoginForm(FlaskForm):
    username = TextField('Username',  [
        validators.Required('Please enter your username.'),
        validators.Length(max=30, message='Username is at most 30 characters.'),
    ])
    password = PasswordField('Password', [
        validators.Required('Please enter a password.'),
        validators.Length(min=6, message='Passwords is at least 6 characters.'),
    ])
    submit = SubmitField('Sign In')

    def __init__(self, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)

    def validate(self):
        if not FlaskForm.validate(self):
            return False

        user =col_user.find_one({"username":self.username.data})
        if user and user.password==self.password.data:
            return True
        else:
            self.password.errors.append('Invalid username or password')
            return False    
