from flask import Markup, url_for
from website.blueprints.main import DOCTORS_DICT

def component (doctor):
    doctor_dict = DOCTORS_DICT[doctor]
    img_src = url_for('static', filename='images/assets/doctor.svg')
    return Markup (f"""

        <div class="doctor_panel_ctnr">
            <div class="img_circle_ctnr">
                <div class="img_ctnr">
                    <img src="{img_src}" alt="doctor svg">
                </div>
            </div>
            <div class="doctor_text_ctnr">
                <h3>
                    {doctor_dict['fname']} {doctor_dict['lname']}
                </h3>
                <small>
                    {doctor_dict['titles']}
                </small>
                <p>
                    {doctor_dict['details1']}
                </p>
                <p>
                    {doctor_dict['details2']}
                </p>
                <p>
                    {doctor_dict['details3']}
                </p>
            </div>
        </div>
    """)