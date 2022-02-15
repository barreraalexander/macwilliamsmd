from flask import Markup, url_for

def component():
    animation = url_for('static', filename='js/interface_mods/menu.js')

    return Markup(f"""
    <div id="hidden_menu" data-status='hidden'>
        <div class="empty">
            <p>
                C <br> L <br> O <br> S <br> E
            </p>

        </div>

        <nav>
            <ul>
                <a href="{url_for('main.index')}">
                    <li>
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
            </ul>
        </nav>
    </div>
    <script src={animation}>
    </script>
    """)