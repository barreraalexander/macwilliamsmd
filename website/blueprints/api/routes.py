from flask import Blueprint, request, redirect, url_for, flash
from website.utils.mail_form import send_contact
from website.utils.mail_form import send_new_client
from website import mail
from datetime import datetime

import json

api = Blueprint ('api', __name__)


@api.route('/send_contact', methods=['GET', 'POST'])
def send_contact():
    form_data = []
    if request.method == 'POST':
        form_data = {
            'fname' : request.form.get('fname'),
            'lname' : request.form.get('lname'),
            'time_sent' : datetime.now(),
            'help_description' : request.form.get('help_description'),
        }
        # response = send_form(form_data)
        response = "hey"
        if response == 'SUCCESS':
            flash ('We got your message!')
            flash (f"We'll contact you at: {form_data['contact_info']}")
        elif response == 'FAIL':
            flash ("There's something wrong on our end. We're working on it now!")
        else:
            flash ("error")
        return redirect(url_for('main.index'))

    return redirect(url_for('main.index'))

@api.route('/send_new_client', methods=['GET', 'POST'])
def send_new_client():
    form_data = []
    if request.method == 'POST':
        form_data = {
            'fname' : request.form.get('fname'),
            'lname' : request.form.get('lname'),
            'time_sent' : datetime.now(),
            'help_description' : request.form.get('help_description'),
        }
        # response = send_new_client(form_data)
        response = "hey"
        if response == 'SUCCESS':
            flash ('We got your message!')
            flash (f"We'll contact you at: {form_data['contact_info']}")
        elif response == 'FAIL':
            flash ("There's something wrong on our end. We're working on it now!")
        else:
            flash ("error")
        return redirect(url_for('main.index'))

    return redirect(url_for('main.index'))
