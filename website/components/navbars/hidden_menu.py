from flask import Markup, url_for

def component():
    return Markup(f"""
    <div id="hidden_menu" data-status='closed'>
        <ul>
            <li>
                <a href="{url_for('main.index')}">
                    Home
                </a>
            </li>
                <li
                <a href="{url_for('main.about')}">
                    About
                </a>
            </li>  
            <li
                <a href="{url_for('main.doctors')}">
                    Doctors
                </a>
            </li>
            <li
                <a href="{url_for('main.services')}">
                    Services
                </a>
            </li>
            <li
                <a href="{url_for('main.contact')}">
                    Contact
                </a>
            </li>  




        </ul>
    </div>

    
    """)