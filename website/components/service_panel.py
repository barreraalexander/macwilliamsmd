from flask import Markup, url_for

def component(service_name):
    img_src = url_for('static', filename=f'images/services/{service_name}_service_circle.png')
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
        <div class="service_ctnr {classes}">
            <div class="picture_title">
                <p>
                    {f_service_title}
                </p>
                <img src="{img_src}" alt="{service_name}" image>
            </div>
            <div class="service_description">
                {service_description}
            </div>
        </div>
    """)