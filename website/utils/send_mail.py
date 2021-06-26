import secrets
from flask_mail import Message
from website import mail
from datetime import datetime
from secrets import token_hex

MAIN_RECIPIENT = "barreraalexander93@gmail.com"

def send_form (form_data):

    msg = Message(f'MAC WILLIAMS MD & ASSOCIATES CONTACT REQUEST | MESSAGE_ID:{token_hex(6)}',
                recipients=[MAIN_RECIPIENT])
    msg.body = (f"""


    FIRST NAME: {form_data['fname']}

    LAST NAME: {form_data['lname']}

    CONTACT INFO: {form_data['contact_info']}

    BEST TIME: {form_data['best_time']}

    COMPANY NAME: {form_data['company_name']}

    COMPANY SIZE: {form_data['company_size'][0]} Employees

    TIME SENT : {form_data['time_sent'].strftime('%B %d, %Y    %I:%M %p')}
    \n
    MESSAGE
    -------
    {form_data['help_description']}
    """)

    try:
        mail.send(msg)
        return 'SUCCESS'
    except Exception as err:
        error_explanation = (f""" Yikes. The email system is down
                    and a user is trying to contact you. This data
                    will be recovered from the virtual machine.
                    ~/website/reports/<log of error id> """)
        print (error_explanation)
        print (err)
        return 'FAIL'
