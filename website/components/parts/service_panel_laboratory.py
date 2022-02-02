from flask import Markup
from website.blueprints.main import SERVICES


def component():
    service_name = "laboratory"
    service_dict = SERVICES[service_name]


    return Markup(f"""
    <section id="{service_name}_service_panel">
        <div class="service_ctnr" data-alt="alt1">
            <h2>
                {service_dict['service_title']}
            </h2>   

            <div class="text_group">
                <h3>
                    {service_dict['heading1']}
                </h3>
                <div class="descriptions_ctnr">
                    <p>
                        {service_dict['description1']}
                    </p>
                </div>
            </div>

            <div class="text_group">
                <h3>
                    {service_dict['heading2']}
                </h3>
                <div class="descriptions_ctnr">
                    <p>
                        {service_dict['description2']}
                    </p>
                </div>
            </div>

            <div class="text_group">
                <h3>
                    {service_dict['heading3']}
                </h3>
                <div class="descriptions_ctnr">
                    <p>
                        {service_dict['description3']}
                    </p>
                </div>
            </div>

            <div class="text_group">
                <h3>
                    {service_dict['heading4']}
                </h3>
                <div class="descriptions_ctnr">
                    <p>
                        {service_dict['description4']}
                    </p>
                </div>
            </div>

            <div class="text_group">
                <h3>
                    {service_dict['heading5']}
                </h3>
                <div class="descriptions_ctnr">
                    <p>
                        {service_dict['description5']}
                    </p>
                </div>
            </div>

            <div class="text_group">
                <h3>
                    {service_dict['heading6']}
                </h3>
                <div class="descriptions_ctnr">
                    <p>
                        {service_dict['description6']}
                    </p>
                </div>
            </div>


            <div class="text_group">
                <h3>
                    {service_dict['heading7']}
                </h3>
                <div class="descriptions_ctnr">
                    <p>
                        {service_dict['description7']}
                    </p>
                </div>
            </div>

            <div class="text_group">
                <h3>
                    {service_dict['heading8']}
                </h3>
                <div class="descriptions_ctnr">
                    <p>
                        {service_dict['description8']}
                    </p>
                </div>
            </div>

            <div class="text_group">
                <h3>
                    {service_dict['heading9']}
                </h3>
                <div class="descriptions_ctnr">
                    <p>
                        {service_dict['description9']}
                    </p>
                </div>
            </div>

            <div class="text_group">
                <h3>
                    {service_dict['heading10']}
                </h3>
                <div class="descriptions_ctnr">
                    <p>
                        {service_dict['description10']}
                    </p>
                </div>
            </div>

        </div>
    </section>

    """)