from flask import Blueprint, request, redirect, url_for, flash
from website.utils.send_mail import send_form
from website.utils.send_mail import send_quick_form
from website import mail
from datetime import datetime

import json

api = Blueprint ('api', __name__)


@api.route('/send_mail', methods=['GET', 'POST'])
def send_mail():
    form_data = []
    if request.method == 'POST':
        form_data = {
            'fname' : request.form.get('fname'),
            'lname' : request.form.get('lname'),
            'contact_info' : request.form.get('contact_info'),
            'best_time' : request.form.get('best_time'),
            'company_name' : request.form.get('company_name'),
            'company_size' : request.form.get('company_size'),
            'time_sent' : datetime.now(),
            'help_description' : request.form.get('help_description'),
        }
        response = send_form(form_data)
        if response == 'SUCCESS':
            flash ('We got your message!')
            flash (f"We'll contact you at: {form_data['contact_info']}")
        elif response == 'FAIL':
            flash ("There's something wrong on our end. We're working on it now!")
        else:
            flash ("error")
        return redirect(url_for('main.index'))

    return redirect(url_for('main.index'))
