from flask import Markup, url_for

def component(slide_name):
    img_src = f"https://macwilliamsmd-static.s3.us-east-2.amazonaws.com/slide_imgs/{slide_name}_cutout.png"
    slide_description = "This is about the service. This is about the service. This is about the service. This is about the service. This is about the service. This is about the service. This is about the service. This is about the service. This is about the service. This is about the service. "
    return Markup(f"""
    <div id="{slide_name}_slide_ctnr" class="slide_ctnr">
        <div class="img_circle_ctnr">
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
            <div class="stripe"></div>
        </div>

    </div>
    """)