from flask import Markup

from website.components.parts.button_like import component as button_like
from website.components.parts.service_grid import component as service_grid
from website.components.parts.service_panel import component as service_panel

from website.components.parts.service_panel_ekg import component as ekg_panel

def component():
    return Markup(f"""
    <section id="services_section">
        <div class="services_banner_ctnr">
            <div class="services_text_ctnr">
                <h1>
                    Our Services
                </h1>
                <p class="service_summary">
                    Summary about our services. Summary about our services. Summary about our services. 
                </p>
                {button_like('appointment')}
            </div>
            {service_grid()}
        </div>

        {ekg_panel()}
        <div class="btn_ctnr">
            {button_like('appointment')}
        </div>
    </section>
    """)