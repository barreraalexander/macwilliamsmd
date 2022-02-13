from fileinput import filename
from flask import Markup, url_for
from website.blueprints.main import INSURANCES, unpack_elems


# make it so that when a user hovers one one image all of the others shrink,
#  and maybe give them a button look, 

def component():
    observer = url_for('static', filename='js/observers/insurances_ctnr.js')

    parts = [
        f"""
        <div
            id="{INSURANCES.get(insurance).get('title')}"
            class="insurance"
        >
            <img
                src={url_for('static', filename=f"/images/insurances/{insurance}.png")}
                alt={insurance}
            >
            <p>
                {INSURANCES.get(insurance).get('title')}
            </p> 
        </div>
        """
        for insurance in INSURANCES
    ]

    return Markup(f"""
    <div class="insurances_ctnr">
        <h2>
            Accepted Insurances
        </h2>
        <div class="insurance_imgs">
            {unpack_elems(parts)}
        </div>
    </div>
    <script src="{observer}">
    </script>
    """)