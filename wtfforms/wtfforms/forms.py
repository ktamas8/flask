from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, DateField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length, URL

class ContactForm(FlaskForm):
    """Contact form."""
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    body = TextAreaField('Message', validators=[DataRequired(), Length(min=4, message=('Your message is too short.'))])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    """Login form."""
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    password = StringField('Password', validators=[DataRequired(), Length(min=8, message=('Your password is too short.'))])
    submit = SubmitField('Submit')

class PrefOSForm(FlaskForm):
    """Openstack preferences form."""
    submit = SubmitField('Submit')

class VMControlForm(FlaskForm):
    """Openstack vm control form."""
    start = SubmitField(label='Start')
    stop = SubmitField(label='Stop')
    pause = SubmitField(label='Pause')
    console = SubmitField(label='Console')
    show = SubmitField(label='Show')

class SignupForm(FlaskForm):
    """Sign up for a user account."""
    email = StringField('Email', [
        Email(message='Not a valid email address.'),
        DataRequired()])
    password = PasswordField('Password', [
        DataRequired(message="Please enter a password."),
    ])
    confirmPassword = PasswordField('Repeat Password', [
            EqualTo(password, message='Passwords must match.')
            ])
    title = SelectField('Title', [DataRequired()],
                        choices=[('Farmer', 'farmer'),
                                 ('Corrupt Politician', 'politician'),
                                 ('No-nonsense City Cop', 'cop'),
                                 ('Professional Rocket League Player', 'rocket'),
                                 ('Lonely Guy At A Diner', 'lonely'),
                                 ('Pokemon Trainer', 'pokemon')])
    website = StringField('Website', validators=[URL()])
    birthday = DateField('Your Birthday')
    submit = SubmitField('Submit')
