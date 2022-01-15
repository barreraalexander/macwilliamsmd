from flask import Markup
from website.components.parts.doctor_panel_lg import component as doctor_panel_lg
from website.components.parts.doctor_card import component as doctor_card

def component():
    return Markup(f"""
    <div class="doctors_ctnr">
        <h2 id="new_doctors_h2">
            Meet Our Doctors
        </h2>
        <div class="doctor_card_ctnr">
            {doctor_card('doctor1')}
            {doctor_card('doctor2')}
        </div>
        <button id="read_more_btn" >
            <a href="{{url_for('main.doctors')}}">
                Read More
            </a>
        </button>
        <div class="doctor_panels_lg_ctnr">
            {doctor_panel_lg('doctor1')}
            <hr>
            {doctor_panel_lg('doctor2')}
        </div>
    </div>

    """)