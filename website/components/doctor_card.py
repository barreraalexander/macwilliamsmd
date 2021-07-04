from flask import Markup, url_for


def component (lname):
    img_src = url_for('static', filename='images/assets/doctor.svg')
    fname = ""
    titles = ""

    if lname=="Williams":
        fname = "Mac"
        titles = "Primary Care Physician"

    elif lname=="Jones":
        fname = "John"
        titles = "Primary Care Physician"

    return Markup (f"""
    <div id="{lname}_doctor_card" class="doctor_card">
        <div class="card_left">
            <p class='name'>
                {lname},
            </p>
            <p class='name'>
                {fname}
            </p>
            <p class='titles'>
                {titles}
            </p>
        </div>
        <div class="card_right">
            <img
                id="{lname}_img"
                src="{img_src}"
                alt="picture of {lname}"
            >

        </div>
    </div>
    
    """)