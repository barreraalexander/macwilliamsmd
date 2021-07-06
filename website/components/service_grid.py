from flask import Markup, url_for


def component():
    learn_more_icon = url_for('static', filename=f'images/assets/more.svg')

    def grid_slot(service):
        img_src = url_for('static', filename=f'images/services/{service}_service_square.png')
        title = ""

        if service=="ekg":
            title = "EKG"

        elif service=="laboratory":
            title = "Lab Work"

        elif service=="radiology":
            title = "Radiology"

        elif service=="gynecology":
            title = "Gynecology"

        return Markup(f"""
        <div class="grid_slot" style="background-image: url('{img_src}');">
            <div class="grid_text">
                <h3>
                    {title}
                </h3>
                <div class="learn_more_ctnr">
                    <p>
                        MORE
                    </p>
                    <img
                        src="{learn_more_icon}"
                    >
                </div>
            </div>
        </div>        
        """)

    return Markup(f"""
    <div class="services_grid_ctnr">
        <div class="grid_row">
            {grid_slot('ekg')}
            {grid_slot('laboratory')}
        </div>
        <div class="grid_row">
            {grid_slot('radiology')}
            {grid_slot('gynecology')}
        </div>
    </div>
    
    """)