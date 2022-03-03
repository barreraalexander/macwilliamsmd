from flask import Markup, url_for

from website.components.parts.slide_text import component as slide_text
from website.components.parts.button_like import component as button_like
from website.components.parts.service_slide import component as service_slide
from website.components.parts.slide_dots_ctnr import component as slide_dots_ctnr

def component():
    return Markup(f"""
    <section id="hero_section">
        <div class="main_display_ctnr">

            <div class="left_col">
                {service_slide('welcome')}
                {service_slide('ekg')}
                {service_slide('laboratory')}
                {service_slide('gynecology')}
                {service_slide('radiology')}
            </div>

            <div class="right_col">
                <img
                    id="welcome_full"
                    src="https://macwilliamsmd-static.s3.us-east-2.amazonaws.com/slide_imgs/welcome_full.png"
                    class="slide_img_full"
                    alt="welcome stock photo"
                >
                <img
                    id="ekg_full"
                    src="https://macwilliamsmd-static.s3.us-east-2.amazonaws.com/slide_imgs/ekg_full.png"
                    class="slide_img_full"
                    alt="ekg stock photo"
                >
                <img
                    id="laboratory_full"
                    src="https://macwilliamsmd-static.s3.us-east-2.amazonaws.com/slide_imgs/laboratory_full.png"
                    class="slide_img_full"
                    alt="laboratory stock photo"
                >
                <img
                    id="gynecology_full"
                    src="https://macwilliamsmd-static.s3.us-east-2.amazonaws.com/slide_imgs/gynecology_full.png"
                    class="slide_img_full"
                    alt="gynecology stock photo"
                >
                <img
                    id="radiology_full"
                    src="https://macwilliamsmd-static.s3.us-east-2.amazonaws.com/slide_imgs/radiology_full.png"
                    class="slide_img_full"
                    alt="radiology stock photo"
                >
            </div>    
        </div>
    </section>


    """)