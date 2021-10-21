from flask import Markup, url_for
from website.blueprints.main import CONTACT_DICT
from website.components.button_like import component as button_like


def component():

    map_src = "https://www.google.com/maps/embed/v1/place?q=place_id:ChIJkR8GEl6h2YgRWx0pMVCxKFc&key=AIzaSyDQ4g571-kVI0g1E7VNHoDXPKxf4B0UpLU"
    logo_src = url_for('static', filename='/images/assets/mac_logo_sqr.svg')

    return Markup(f"""

    <section id="base_footer_section">
        <div id="footer_actions_ctnr">
            <div class="action_ctnr">
                <h2>
                    Location
                </h2>
                <i>
                    {CONTACT_DICT['address']}
                </i>
                {button_like(btn_type='navigation')}
            </div>
            <div class="action_ctnr">
                <h2>
                    Appointments
                </h2>
                {button_like(btn_type='phone')}
            </div>
            <div class="action_ctnr">
                <h2>
                    Questions
                </h2>
                {button_like(btn_type='phone2')}
            </div>
            <div class="action_ctnr">
                <h2>
                    Message Us
                </h2>
                {button_like(btn_type='send')}
            </div>
            <!-- <div class="action_ctnr">
                <h2>
                    New Client
                </h2>
                {button_like(btn_type='send')}
            </div> -->
        </div>

        <hr>
        

        <div id="office_hours_ctnr">
            <h2>
                Office Hours
            </h2>
            <div class="office_hour">
                <p class="date">
                    Monday
                </p>
                <p class="time">
                    8:00am - 5:00pm
                </p>
            </div>
            <div class="office_hour">
                <p class="date">
                    Tuesday
                </p>
                <p class="time">
                    8:00am - 5:00pm
                </p>
            </div>
            <div class="office_hour">
                <p class="date">
                    Wednesday
                </p>
                <p class="time">
                    8:00am - 5:00pm
                </p>
            </div>
            <div class="office_hour">
                <p class="date">
                    Thursday
                </p>
                <p class="time">
                    8:00am - 5:00pm
                </p>
            </div>
            <div class="office_hour">
                <p class="date">
                    Friday
                </p>
                <p class="time">
                    8:00am - 5:00pm
                </p>
            </div>
            <div class="office_hour">
                <p class="date">
                    Saturday
                </p>
                <p class="time">
                    Closed
                </p>
            </div>
            <div class="office_hour">
                <p class="date">
                    Sunday
                </p>
                <p class="time">
                    Closed
                </p>
            </div>
        </div>
    
        <div id="tos_ctnr">
            <a href="#">
                Terms of Service
            </a>
            <a href="#">
                Legal Stuff
            </a>
            <a href="#">
                Sitemap
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