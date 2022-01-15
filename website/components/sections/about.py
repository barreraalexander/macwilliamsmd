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
                            A team of experts in a range of medical specialties, we cover the South Florida region and are proud of a reputation for excellent service and a professional yet welcoming approach. With many years of experience behind them our team are all fully qualified in their area of expertise and we guarantee you will be treated with the care and attention you deserve. 
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
                        Our specialist areas include the following:
                    </p>
                    <ul>
                        <li>
                            Lab work including Complete Blood Count, Metabolic Panels, Liver Panels and more, plus all areas of lab work including cultures. 
                        </li>
                        <li>
                            Gynecology including the specialized area of endocrinology, pelvic malignancy, female urology, and all areas of women’s health.
                        </li>
                        <li>
                            Radiology solutions including X-ray, CT scans, MRI, and all the very latest in diagnostic radiology procedures.
                        </li>
                    </ul>
                    <p>
                        While the above is not a comprehensive list of our services and solutions it does outline the areas in which we believe we can provide the best service in the South Florida region. We're here to help patients who need expert treatment and with many satisfied clients who testify to our excellence, we are committed to being the best in all areas of the medical field in which we profess expertise. You can find full details of our services at our website where you will also see contact details. We also invite you to check out our doctor's biographies on the website so you can see where our highly skilled and professionally trained team gained their education and work experience. Please contact us now if you need our help and one of the team will be happy to discuss your situation.
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