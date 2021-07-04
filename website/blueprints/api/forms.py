from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from datetime import datetime

#//SECTION: AUTHENTICATION
class ContactUsForm (FlaskForm):
    fname = StringField('First Name and Last Name',
                        validators=[DataRequired(),
                        Length(min=2, max=30)],
                        render_kw={"placeholder":"John Doe"})
   

    contact_info = StringField ('PHONE NUMBER OR EMAIL',
                        validators=[DataRequired(),
                        Length(min=2, max=50)],
                        render_kw={"placeholder":"Your Phone Number or Email"})
   
    best_time = StringField ('BEST TIME TO REACH YOU',
                        validators=[Length(min=1, max=50)],
                        render_kw={"placeholder":"Weekdays 9AM"})
   
    company_name = StringField ('COMPANY NAME',
                        validators=[DataRequired(),
                        Length(min=2, max=50)],
                        render_kw={"placeholder":"Your Company's Name"})

    company_size = SelectMultipleField ('COMPANY SIZE',
                        validators=[DataRequired(),
                        Length(min=2, max=50)])

    help_description = TextAreaField ('HOW CAN WE HELP',
                        validators=[Length(min=2, max=300)],
                        render_kw={"placeholder":"Your Message"})

    recaptcha = RecaptchaField()

    time_sent = StringField ('Time Sent',
                            default=datetime.now())

    submit = SubmitField('SUBMIT')

class NewClientForm (FlaskForm):
    fname = StringField('First Name and Last Name',
                        validators=[DataRequired(),
                        Length(min=2, max=30)],
                        render_kw={"placeholder":"John Doe"})
   

    contact_info = StringField ('PHONE NUMBER OR EMAIL',
                        validators=[DataRequired(),
                        Length(min=2, max=50)],
                        render_kw={"placeholder":"Your Phone Number or Email"})
   
    best_time = StringField ('BEST TIME TO REACH YOU',
                        validators=[Length(min=1, max=50)],
                        render_kw={"placeholder":"Weekdays 9AM"})
   
    company_name = StringField ('COMPANY NAME',
                        validators=[DataRequired(),
                        Length(min=2, max=50)],
                        render_kw={"placeholder":"Your Company's Name"})

    company_size = SelectMultipleField ('COMPANY SIZE',
                        validators=[DataRequired(),
                        Length(min=2, max=50)])

    help_description = TextAreaField ('HOW CAN WE HELP',
                        validators=[Length(min=2, max=300)],
                        render_kw={"placeholder":"Your Message"})

    recaptcha = RecaptchaField()

    time_sent = StringField ('Time Sent',
                            default=datetime.now())

    submit = SubmitField('SUBMIT')