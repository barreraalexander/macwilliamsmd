from flask import Markup, url_for

from website.components.parts.button_like import component as button_like
from website.components.parts.service_grid import component as service_grid

from website.components.parts.service_panel_ekg import component as ekg_panel
from website.components.parts.service_panel_laboratory import component as lab_panel
from website.components.parts.service_panel_radiology import component as rad_panel
from website.components.parts.service_panel_gynecology import component as gyn_panel
def component():
    observer = url_for('static', filename='js/observers/services.js')

    return Markup(f"""
    <section id="services_section">
        <a href="#base_header_section">
            <button id="back_to_top">            
                ^
            </button>
        </a>
        <div class="services_banner_ctnr">
            <div class="services_text_ctnr">
                <h1>
                    Our Services
                </h1>
                {button_like('appointment')}
            </div>
            {service_grid()}
        </div>

        {ekg_panel()}
        {lab_panel()}
        {rad_panel()}
        {gyn_panel()}
        <div class="btn_ctnr">
            {button_like('appointment')}
        </div>
    </section>
    <script src="{observer}">
    </script>
    """)