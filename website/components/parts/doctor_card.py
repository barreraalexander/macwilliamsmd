from flask import Markup, url_for
from website.blueprints.main import DOCTORS_DICT

def component (doctor):
    doctor_dict = DOCTORS_DICT[doctor]
    img_src = url_for('static', filename='images/assets/doctor.svg')

    return Markup (f"""
    <div id="{doctor_dict['lname']}_doctor_card" class="doctor_card">
        <div class="card_left">
            <p class='name'>
                {doctor_dict['lname']},
            </p>
            <p class='name'>
                doctor_dict['fname']
            </p>
            <p class='titles'>
                {doctor_dict['titles']}
            </p>
        </div>
        <div class="card_right">
            <img
                id="{doctor_dict['lname']}_img"
                src="{img_src}"
                alt="picture of {doctor_dict['lname']}"
            >
        </div>
    </div>
    
    """)