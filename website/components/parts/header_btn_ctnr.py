from flask import Markup, url_for
from website.blueprints.main import CONTACT_DICT



def component():

    contact_link = url_for('main.contact')
    appointment_src = url_for('static', filename='images/assets/appointment.svg')
    phone_src = url_for('static', filename='images/assets/call_navy.svg')


    return Markup(f"""    
    <div id="header_btn_ctnr">
        <div id="header_book_btn">
            <img
                src="{appointment_src}"
                alt="appointment icon"
            >
            <a href="{contact_link}">
                Appointments
            </a>
        </div>
        <div id="header_phone_btn">
            <img
                src="{phone_src}"
                alt="phone icon"
            >
            <a href="tel:{CONTACT_DICT['phone']}">
                {CONTACT_DICT['phone']}
            </a>
        </div>
    </div>




    
    """)