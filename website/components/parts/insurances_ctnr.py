from flask import Markup
from website.blueprints.main import INSURANCES


def component():



    return Markup(f"""
    <div class="insurances_ctnr">
        <h2>
            Insurances that we Accept
        </h2>
        <div class="insurance_imgs">

            
        </div>
    </div>    
    """)