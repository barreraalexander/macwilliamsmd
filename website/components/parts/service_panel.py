from flask import Markup, url_for
from website.blueprints.main import SERVICES

def component(service_name):
    img_sm_src = f"https://macwilliamsmd-static.s3.us-east-2.amazonaws.com/service_imgs/{service_name}_service_circle.png"
    img_lg_src = f"https://macwilliamsmd-static.s3.us-east-2.amazonaws.com/service_imgs/{service_name}_service_square.png"
    classes = ""
    lazy_dataset = ""

    if service_name=='laboratory' or service_name=='gynecology':
        classes="inverse_service_panel"

    service_dict = SERVICES[service_name]
    # service_dict = SERVICES['ekg']

    return Markup(f"""
        <div id="{service_name}_panel" class="service_ctnr {classes}">
            <div class="picture_title">
                <p class="sm_service_title">
                    {service_dict['service_title']}
                </p>
                <img
                    class="sm_service_img"
                    src="{img_sm_src}"
                    alt="{service_name} image"
                >
                <img
                    class="lg_service_img"
                    src="{img_lg_src}"
                    alt="{service_name} image"
                    {lazy_dataset}
                >
            </div>
            <div class="service_description">
                <p class="lg_service_title">
                    {service_dict['service_title']}
                </p>
                <p>
                    {service_dict['service_title']}
                </p>
            </div>
        </div>
    """)