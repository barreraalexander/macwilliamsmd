from flask import Markup, url_for
from website.blueprints.main import SERVICES, ABOUT_US

# from website.components.parts.slide_text import component as slide_text
from website.components.parts.button_like import component as button_like
# from website.components.parts.service_slide import component as service_slide
from website.components.parts.slide_dots_ctnr import component as slide_dots_ctnr

def component(slide_name):

    service = SERVICES.get(slide_name)
    link = url_for('main.services')+f'#{slide_name}_service_panel'


    if not service:
        service = {
            'slide_text' : ABOUT_US.get('slide_text'),
            'link' : url_for('main.services'),
            'slide_h1' : 'Mac Williams MD',
            'slide_small' : '& Associates',
        }

    img_src = f"https://macwilliamsmd-static.s3.us-east-2.amazonaws.com/slide_imgs/{slide_name}_cutout.png"

    slide_description = service.get('slide_text')

    slide_description2 = service.get('description1')

    return Markup(f"""
    <div id="{slide_name}_slide_ctnr" class="slide_ctnr">

        <div id="{slide_name}_slide_text" class="slide_text_ctnr">
            <h1 id="slide_h1">
                {service.get("slide_h1")}
            </h1>
            <small id="slide_small">
                {service.get("slide_small")}
            </small>
        </div>

        {slide_dots_ctnr()}
    
        <div class="small_slide">
            <div class="img_ctnr">
                <img
                    id="{slide_name}_img"
                    src="{img_src}"
                    alt="{slide_name}"
                />
            </div>
        </div>


        <div class="slide_description_ctnr">
            <p>
                {slide_description}
            </p>
            <div class="hidden_text">
                <p>
                    {slide_description2}
                </p>
            </div>
            <a href="{link}">
                <p class="link">
                    Learn More
                </p>
            </a>
            <div class="stripe"></div>
        </div>
    </div>
    """)

    # return Markup(f"""
    # <div id="{slide_name}_slide_ctnr" class="slide_ctnr">
    #     <div class="img_circle_ctnr">
    #         <div class="img_ctnr">
    #             <img
    #                 id="{slide_name}_img"
    #                 src="{img_src}"
    #                 alt="{slide_name}"
    #             />
    #         </div>
    #     </div>

    #     <div class="slide_description_ctnr">
    #         <p>
    #             {slide_description}
    #         </p>
    #         <div class="hidden_text">
    #             <p>
    #                 {slide_description2}
    #             </p>
    #         </div>
    #         <a href="{link}">
    #             <p class="link">
    #                 Learn More
    #             </p>
    #         </a>
    #         <div class="stripe"></div>
    #     </div>
    # </div>
    # """)