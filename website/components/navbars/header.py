from flask import Markup, url_for
from website.blueprints.main import CONTACT_DICT
from website.components.navbars.linkset import component as linkset
from website.components.parts.button_like import component as button_like

def component():
    home_link = url_for('main.index')    
    contact_link = url_for('main.contact')

    logo_src = url_for('static', filename='images/assets/mac_logo_banner.svg')
    menu_src = url_for('static', filename='images/assets/hamburger_lblue.svg')
    appointment_src = url_for('static', filename='images/assets/appointment.svg')
    phone_src = url_for('static', filename='images/assets/call_navy.svg')
    
    return Markup(f"""
    <section id="base_header_section">
        <aside>
            <nav>
                <ul class="main_nav_ul">
                    <li id="logo_ctnr">
                        <a href="{home_link}">
                            <img
                                id="mac_banner"
                                src="{logo_src}"
                                alt="mac williams md logo"
                            >
                        </a>
                    </li>
                    <li id="hamburger_ctnr">
                        <img
                            id="hamburger"
                            src="{menu_src}"
                            alt="mobile navigation button"
                        >
                    </li>
                    {linkset("tablet")}
                    <li id="patient_portal_ctnr" dataset-mquery="tablet">
                        {button_like('patient')}
                    </li>
                    <li id="book_appointment_ctnr" dataset-mquery="tablet">
                        {button_like('appointment', elem_id='header_appointment')}
                    </li>
                </ul>
            </nav>
            <div id="header_btn_ctnr">
                <div id="header_book_btn">
                    <img
                        src="{appointment_src}"
                        alt="appointment icon"
                    >
                    <a href="{contact_link}">
                        Appointments
                    </a>
                </div>
                <div id="header_phone_btn">
                    <img
                        src="{phone_src}"
                        alt="phone icon"
                    >
                    <a href="tel:{CONTACT_DICT['phone']}">
                        {CONTACT_DICT['phone']}
                    </a>
                </div>
            </div>
            <div id="hidden_menu" data-status='closed'>
                <ul>
                    {linkset("hidden_menu")}
                </ul>
            </div>
        </aside>

    </section>

    
    
    """)