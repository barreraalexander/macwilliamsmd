from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from datetime import datetime

class ContactUsForm (FlaskForm):
    fname = StringField('Name',
                        validators=[DataRequired(),
                        Length(min=2, max=30)],
                        render_kw={"placeholder":"John Doe"})
   

    email = StringField ('Email',
                        validators=[DataRequired(),
                        Length(min=2, max=50)],
                        render_kw={"placeholder":"Email"})
   
    help_description = TextAreaField ('How Can We Help',
                        validators=[Length(min=2, max=300)],
                        render_kw={"placeholder":"Your Message"})

    recaptcha = RecaptchaField()

    time_sent = StringField ('Time Sent',
                            default=datetime.now())

    submit = SubmitField('SUBMIT')
