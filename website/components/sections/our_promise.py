from flask import Markup, url_for
from website.blueprints.main import ABOUT_US


def component():
    gif_src = url_for('static', filename='images/gifs/tree_anim.gif')
    observer = url_for('static', filename='js/observers/our_promise.js')


    return Markup(f"""
    <section id="our_promise_section">
        <div class="gif_ctnr">
            <img
                src="{gif_src}"
            >
        </div>
        <div class="mission_statement_ctnr">
            <h2>
                Our Promise
            </h2>
            <p>
                {ABOUT_US.get('description1')}
            </p>
            <p>
                {ABOUT_US.get('description4')}
            </p>
        </div>
    </section>
    <script src="{observer}">
    </script>
    
    
    """)