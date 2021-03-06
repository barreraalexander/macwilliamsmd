from flask import Markup, url_for
from website.blueprints.main import CONTACT_DICT

def component(btn_type, elem_id=''):
    img_src = ""
    classes = ""
    btn_text = ""
    link = ""

    if btn_type=='navigation':
        img_src = url_for('static', filename='images/assets/navigation.svg')
        classes = "inverse_btn_like"
        btn_text = "Navigate Here"

    elif btn_type=='phone':
        img_src = url_for('static', filename='images/assets/call.svg')
        classes = "standard_btn_like apply_wiggle"
        btn_text = CONTACT_DICT['phone']
        link = f"tel:{CONTACT_DICT['phone']}"

    elif btn_type=='phone2':
        img_src = url_for('static', filename='images/assets/call.svg')
        classes = "standard_btn_like apply_wiggle"
        btn_text = CONTACT_DICT['phone2']

    elif btn_type=='send':
        img_src = url_for('static', filename='images/assets/send.svg')
        classes = "standard_btn_like"
        btn_text = "FILL OUT THE FORM"
        link = url_for('main.contact')

    elif btn_type=='submit':
        img_src = url_for('static', filename='images/assets/send.svg')
        classes = "standard_btn_like"
        btn_text = "SUBMIT"

    elif btn_type=='patient':
        img_src = url_for('static', filename='images/assets/person_navy.svg')
        classes = "inverse_btn_like"
        btn_text = "Patient Portal"

    elif btn_type=='appointment':
        img_src = url_for('static', filename='images/assets/appointment.svg')
        classes = "standard_btn_like appointment_btn"
        btn_text = "Appointments"
        link = url_for('main.contact')

        if elem_id=="header_appointment":    
            img_src = url_for('static', filename='images/assets/appointment_navy.svg')
            classes = "inverse_btn_like appointment_btn"


    return Markup (f"""
        <a href="{link}">
            <div id="{elem_id}" class="button_like {classes}">
                <img
                src="{img_src}"
                alt="navigation img"
                >
                    <p>
                        {btn_text}
                    </p>
            </div>
        </a>
        
    """)