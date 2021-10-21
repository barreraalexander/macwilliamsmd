from flask import Markup, url_for

def component(list_type="hidden_menu"):
    mquery = ""

    if list_type=="tablet":
        mquery = "dataset-mquery='tablet'"

    return Markup(f"""
                    <li {mquery} data-active='true'>
                        <a href="{url_for('main.index')}">
                            Home
                        </a>
                    </li>
                        <li {mquery}>
                        <a href="{url_for('main.about')}">
                            About
                        </a>
                    </li>  
                    <li {mquery}>
                        <a href="{url_for('main.doctors')}">
                            Doctors
                        </a>
                    </li>
                    <li {mquery}>
                        <a href="{url_for('main.services')}">
                            Services
                        </a>
                    </li>
                    <li {mquery}>
                        <a href="{url_for('main.contact')}">
                            Contact
                        </a>
                    </li>  

    """)