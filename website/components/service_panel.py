from flask import Markup, url_for

def component(service_name):
    img_sm_src = f"https://macwilliamsmd-static.s3.us-east-2.amazonaws.com/service_imgs/{service_name}_service_circle.png"
    img_lg_src = f"https://macwilliamsmd-static.s3.us-east-2.amazonaws.com/service_imgs/{service_name}_service_square.png"
    classes = ""

    if service_name=="ekg":
        f_service_title = "EKG"
        service_description = "This is a summary about the service. This is a summary about the service. This is a summary about the service. This is a summary about the service."

    elif service_name=="laboratory":
        f_service_title = "Lab Work"
        classes = "inverse_service_panel"
        service_description = "This is a summary about the service. This is a summary about the service. This is a summary about the service. This is a summary about the service."

    elif service_name=="radiology":
        f_service_title = "Radiology"
        service_description = "This is a summary about the service. This is a summary about the service. This is a summary about the service. This is a summary about the service."

    elif service_name=="gynecology":
        f_service_title = "Gynecology"
        classes = "inverse_service_panel"
        service_description = "This is a summary about the service. This is a summary about the service. This is a summary about the service. This is a summary about the service."

    return Markup(f"""
        <div id="{service_name}_panel" class="service_ctnr {classes}">
            <div class="picture_title">
                <p class="sm_service_title">
                    {f_service_title}
                </p>
                <img class="sm_service_img" src="{img_sm_src}" alt="{service_name}" image>
                <img class="lg_service_img" src="{img_lg_src}" alt="{service_name}" image>
            </div>
            <div class="service_description">
                <p class="lg_service_title">
                    {f_service_title}
                </p>
                <p>
                    {service_description}
                </p>
            </div>
        </div>
    """)