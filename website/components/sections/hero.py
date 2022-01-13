from flask import Markup

from website.components.parts.slide_text import component as slide_text
from website.components.parts.button_like import component as button_like
from website.components.parts.service_slide import component as service_slide

def component():
    return Markup(f"""
    <section id="hero_section">
        <div class="main_display_ctnr">
            <div class="left_col">
                {slide_text('welcome')}
                {slide_text('ekg')}
                {slide_text('laboratory')}
                {slide_text('radiology')}
                {slide_text('gynecology')}
                <div class="slide_dots_ctnr">
                    <div
                        class="slide_dot"
                        data-active='true'
                        data-panel_id="welcome_slide_ctnr"
                        data-full_img_id="welcome_full"
                        data-text_id="welcome_slide_text"
                        data-slide_index=0
                    >
                    </div>
                    <div
                        class="slide_dot"
                        data-panel_id="ekg_slide_ctnr"
                        data-full_img_id="ekg_full"
                        data-text_id="ekg_slide_text"
                        data-slide_index=1
                    >
                    </div>
                    <div
                        class="slide_dot"
                        data-panel_id="laboratory_slide_ctnr"
                        data-full_img_id="laboratory_full"
                        data-text_id="laboratory_slide_text"
                        data-slide_index=2
                    >
                    </div>
                    <div
                        class="slide_dot"
                        data-panel_id="radiology_slide_ctnr"
                        data-full_img_id="radiology_full"
                        data-text_id="radiology_slide_text"
                        data-slide_index=3
                    >
                    </div>
                    <div
                        class="slide_dot"
                        data-panel_id="gynecology_slide_ctnr"
                        data-full_img_id="gynecology_full"
                        data-text_id="gynecology_slide_text"
                        data-slide_index=4
                    >
                    </div>
                </div>
    
                <div id="slider_ctnr">
                    { service_slide('welcome')}
                    { service_slide('ekg') }
                    { service_slide('laboratory')}
                    { service_slide('radiology') }
                    { service_slide('gynecology')}
                </div>

                <div class="buttons_ctnr">
                    { button_like('appointment') }
                    { button_like('phone') }
                </div>
        
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