from flask import Markup, url_for
from website.blueprints.main import CONTACT_DICT, ABOUT_US
from website.components.parts.doctor_panel_lg import component as doctor_panel
from website.components.parts.button_like import component as button_like

def component():
    observer = url_for('static', filename='js/observers/about.js')

    return Markup(f"""
    <section id="about_section">
        <div class="banner_ctnr">
            <h1>
                About our Practice
            </h1>
            <h2>
                Mac Williams MD
                <br>
                & Associates
            </h2>
            {button_like('appointment')}
        </div>

        <div class="description1_ctnr">
            <p>
                {ABOUT_US['description1']}
            </p>
        </div>
        
        
        <div class="ul_ctnr">
            <p>
                {ABOUT_US['ul_heading']}
            </p>
            <ul>
                <li>
                    {ABOUT_US['li1']}
                </li>
                <li>
                    {ABOUT_US['li2']}
                </li>
                <li>
                    {ABOUT_US['li3']}
                </li>
            </ul>
        </div>
        
        <div class="about_row">
            <img
                src="https://macwilliamsmd-static.s3.us-east-2.amazonaws.com/service_imgs/about_us.jpg"
                alt="about us stock photo"
            >
            <p>
                {ABOUT_US['description2']}
            </p>

            <p>
                {ABOUT_US['description3']}
            </p>

            <p>
                {ABOUT_US['description4']}
            </p>
        </div>
        
        
        <div class="about_doctor_ctnr">
            <h1>
                Meet our Doctors
            </h1>
            <div class="about_doctor_panels_lg_ctnr">
                {doctor_panel('doctor1')}
            </div>
        </div>

    </section>
    <script src="{observer}">
    </script>
    
    """)