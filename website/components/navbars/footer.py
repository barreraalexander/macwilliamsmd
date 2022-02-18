from flask import Markup, url_for
from website.blueprints.main import CONTACT_DICT
from website.components.parts.button_like import component as button_like
from website.components.parts.office_hours_ctnr import component as office_hours_ctnr

def component():

    map_src = "https://www.google.com/maps/embed/v1/place?q=place_id:ChIJkR8GEl6h2YgRWx0pMVCxKFc&key=AIzaSyDQ4g571-kVI0g1E7VNHoDXPKxf4B0UpLU"
    logo_src = url_for('static', filename='/images/assets/mac_logo_sqr.svg')
    return Markup(f"""

    <section id="base_footer_section">
        <div id="footer_actions_ctnr">
            <div class="action_ctnr">
                <h2>
                    Locations
                </h2>
                <p class="addr">
                    {CONTACT_DICT.get('address_city1')} | <span> {CONTACT_DICT.get('address1')} <span>
                </p>
                <p class="addr">
                    {CONTACT_DICT.get('address_city2')} | <span> {CONTACT_DICT.get('address2')} <span>
                </p>
            </div>

            <div class="action_ctnr">
                <h2>
                    Questions
                </h2>
                {button_like(btn_type='phone')}
            </div>
            <div class="action_ctnr">
                <h2>
                    Message Us
                </h2>
                {button_like(btn_type='send')}
            </div>
        </div>

        <hr>
        
        {office_hours_ctnr('office1')}

        <hr>
        
        {office_hours_ctnr('office2')}
    
        <div id="tos_ctnr">
            <a href="#">
                <p>
                    Terms of Service
                </p>
            </a>
            <a href="#">
                <p>
                    Legal Stuff
                </p>
            </a>
            <a href="#">
                <p>
                    Sitemap
                </p>
            </a>
        </div>

        <div class="map_widget_ctnr">
            <iframe
                width="100%"
                height="100%"
                style="border:0"
                loading="lazy"
                allowfullscreen
                src="{map_src}"
            ></iframe>
        </div>

        <div class="last_logo_ctnr">
            <img
                src="{logo_src}"
                alt="Mac Williams & Associates Logo"
            >
        </div>
        <div id="top_btn_ctnr">
            <a href="#base_header_section">
                <button id="to_top_btn">
                    BACK TO THE TOP
                </button>                
            </a>
        </div>

    </section>
    """)