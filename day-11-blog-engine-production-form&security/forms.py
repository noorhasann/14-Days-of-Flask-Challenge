from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class SignupForm(FlaskForm):
    username = StringField(
        "Username", 
        validators=[DataRequired(), Length(min=3, max=20)]
    )
    email = StringField(
        "Email", 
        validators=[DataRequired(), Email(message="Invalid email address")]
    )
    password = PasswordField(
        "Password", 
        validators=[DataRequired(), Length(min=8, message="Password must be at least 8 characters long")]
    )
    confirm_password = PasswordField(
        "Confirm Password", 
        validators=[DataRequired(), EqualTo('password', message='Passwords must match')]
    )
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(message="Username zaroori hai!")
    ])
    password = PasswordField(
        "Password", 
        validators=[DataRequired()]
    )
    submit = SubmitField("Login")


class PostForm(FlaskForm):
    title = StringField(
        "Title", 
        validators=[DataRequired(), Length(max=100)]
    )
    content = TextAreaField(
         "Content", 
        validators=[DataRequired()]
    )
    submit = SubmitField("Publish Post")