from flask import Markup
from website.blueprints.main import CONTACT_DICT
from website.components.parts.doctor_panel_lg import component as doctor_panel
from website.components.parts.button_like import component as button_like

def component():
    return Markup(f"""
    <section id="about_section">
        <div class="banner_ctnr">
            <h1>
                About our Practice
            </h1>
        </div>


        <div id="about_header_ctnr">
            <div class="about_banner_ctnr">
                <div class="about_row">
                    <div class="row_text_ctnr">
                        <h2>
                            Mac Williams MD
                            <br>
                            & Associates
                        </h2>
                        <small>
                            {CONTACT_DICT['address']}
                        </small>
                        <div id="btn_ctnr">
                            {button_like('appointment')}  
                        </div>
                        <p>
                            This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. 
                            This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. 
                            This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. 
                            This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. 
                        </p>
                    </div>
                    <div class="row_img_ctnr">
                        <img
                            src="https://macwilliamsmd-static.s3.us-east-2.amazonaws.com/service_imgs/about_us.jpg"
                            alt="about us stock photo"
                        >
                    </div>
                </div>


                <div class="about_row">
                    <p>
                        This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. 
                        This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. 
                        This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. 
                    </p>
                    <p class="hidden_about">
                        This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. 
                        This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. 
                        This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. This is about us. 
                    </p>
                </div>
            </div>



        </div>

        <div class="about_doctor_ctnr">
            <h1>
                Meet our Doctors
            </h1>
            <div class="about_doctor_panels_lg_ctnr">
                {doctor_panel('doctor1')}
                {doctor_panel('doctor2')}
            </div>
        </div>
    </section>
    """)