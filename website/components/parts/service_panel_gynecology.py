from flask import Markup
from website.blueprints.main import SERVICES


def component():
    service_name = "gynecology"
    service_dict = SERVICES[service_name]


    return Markup(f"""
    <section id="{service_name}_service_panel">
        <div class="service_ctnr" data-alt="alt2">
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
                    <p>
                        {service_dict['description2']}
                    </p>
                </div>
            </div>
            

            <div class="text_group">
                <h4>
                    {service_dict['ul1_heading']}
                </h4>
                <ul>
                    <li>
                        {service_dict['ul1_li1']}
                    </li>
                    <li>
                        {service_dict['ul1_li2']}
                    </li>
                    <li>
                        {service_dict['ul1_li3']}
                    </li>
                    <li>
                        {service_dict['ul1_li4']}
                    </li>
                </ul>
                <p>
                    {service_dict['ul1_footer']}
                </p>    
            </div>



            <div class="text_group">
                <h3>
                    {service_dict['heading2']}
                </h3>
                <h4>
                    {service_dict['ul2_heading']}
                </h4>
                <ul>
                    <li>
                        {service_dict['ul2_li1_bold']}
                        {service_dict['ul2_li1']}
                    </li>
                    <li>
                        {service_dict['ul2_li2_bold']}
                        {service_dict['ul2_li2']}
                    </li>
                    <li>
                        {service_dict['ul2_li3_bold']}
                        {service_dict['ul2_li3']}
                    </li>
                </ul>
            </div>

            <div class="text_group">
                <h3>
                    {service_dict['heading3']}
                </h3>
                <div class="descriptions_ctnr">
                    <p>
                        {service_dict['description3']}
                    </p>
                    <p>
                        {service_dict['description4']}
                    </p>
                    <p>
                        {service_dict['description5']}
                    </p>
                    <p>
                        {service_dict['description6']}
                    </p>
                </div>
            </div>
        </div>            
    </section">
    """)