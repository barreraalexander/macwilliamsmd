from flask import Markup, url_for
from website.components.parts.button_like import component as button_like

from website.components.parts.header_btn_ctnr import component as header_btn_ctnr
from website.components.navbars.hidden_menu import component as hidden_menu

def component():

    logo_src = url_for('static', filename='images/assets/mac_logo_banner.svg')
    menu_src = url_for('static', filename='images/assets/hamburger_lblue.svg')

    return Markup(f"""
    <section id="base_header_section">
        <nav>

            <ul class="main_nav_ul">

                <a href="{ url_for('main.index') }">
                    <li id="logo_ctnr">
                        <img
                            id="mac_banner"
                            src="{logo_src}"
                            alt="mac williams md logo"
                        >
                    </li>
                </a>

                <li id="hamburger_ctnr">
                    <img
                        id="hamburger"
                        src="{menu_src}"
                        alt="mobile navigation button"
                    >
                </li>

                <div class="hidden_links">
                    <a href="{url_for('main.index')}">
                        <li id="home">
                            Home
                        </li>
                    </a>

                    <a href="{url_for('main.about')}">
                        <li>
                            About
                        </li>  
                    </a>

                    <a href="{url_for('main.doctors')}">
                        <li>
                            Doctors
                        </li>
                    </a>

                    <a href="{url_for('main.services')}">
                        <li>
                            Services
                        </li>
                    </a>

                    <a href="{url_for('main.contact')}">
                        <li>
                                Contact
                        </li>
                    </a>

                    {button_like('patient')}

                    {button_like('appointment', elem_id='header_appointment')}
                </div>
            </ul>
        </nav>

        {header_btn_ctnr()}

        {hidden_menu()}

    </section>

    """)