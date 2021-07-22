from flask import Markup, url_for
from website.blueprints.main import DOCTORS_DICT

def component (doctor):
    doctor_dict = DOCTORS_DICT[doctor]
    img_src = url_for('static', filename='images/assets/doctor.svg')
    return Markup (f"""
        <div class="doctor_panel_lg_ctnr">
            <img src="{img_src}" alt="doctor svg">
            <h3>
                {doctor_dict['fname']} {doctor_dict['lname']}
            </h3>
            <p>
                {doctor_dict['titles']}
            </p>
        </div>
    """)