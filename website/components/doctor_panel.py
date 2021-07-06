from flask import Markup, url_for

def component (lastname):
    firstname = "Mac"
    titles = "MD, PA, Primary Care Physician"
    details = "This is about the doctor. This is about the doctor. This is about the doctor. This is about the doctor. This is about the doctor. This is about the doctor. This is about the doctor. This is about the doctor. This is about the doctor. This is about the doctor. This is about the doctor. This is about the doctor. This is about the doctor. This is about the doctor. This is about the doctor. This is about the doctor. This is about the doctor. This is about the doctor. "
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
                    {firstname} {lastname}
                </h3>
                <small>
                    {titles}
                </small>
                <p>
                    {details}
                </p>
            </div>
        </div>

    """)