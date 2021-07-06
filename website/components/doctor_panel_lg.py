from flask import Markup, url_for

def component (lastname):
    firstname = "Mac"
    titles = "MD, PA, Primary Care Physician"
    img_src = url_for('static', filename='images/assets/doctor.svg')
    return Markup (f"""
        <div class="doctor_panel_lg_ctnr">
            <img src="{img_src}" alt="doctor svg">
            <h3>
                {firstname} {lastname}
            </h3>
            <p>
                {titles}
            </p>
        </div>
    """)