from flask import Markup
from website.blueprints.main import SERVICES

def component(lazy=False):
    service_name = 'ekg'
    service_dict = SERVICES[service_name]

    img_sm_src = f"https://macwilliamsmd-static.s3.us-east-2.amazonaws.com/service_imgs/{service_name}_service_circle.png"
    img_lg_src = f"https://macwilliamsmd-static.s3.us-east-2.amazonaws.com/service_imgs/{service_name}_service_square.png"


    lazy_dataset = ""
    if lazy:
        lazy_dataset = "loading='lazy'"

    classes = ""


    return Markup(f"""
    <div class="service_ctnr">
        
    </div>

    
    """)

    return Markup(f"""
    <div id="{service_name}_panel" class="service_ctnr">
        <div class="service_header">
            <div class="picture_title">
                <p class="sm_service_title">
                    {service_dict['service_title']}
                </p>
                <img
                    class="sm_service_img"
                    src="{img_sm_src}"
                    alt="{service_name} image"
                >
                <img
                    class="lg_service_img"
                    src="{img_lg_src}"
                    alt="{service_name} image"
                    {lazy_dataset}
                >
            </div>
        
            <div>
                <p class="lg_service_title">
                    {service_dict['service_title']}
                </p>            
                <p class="service_heading">
                    {service_dict['heading1']}
                </p>
                <p>
                    {service_dict['description1']}
                </p>    
            </div>            
        </div>

        <div class="service_description">
        
            <div class="descriptions_ctnr">
                <p> 
                    {service_dict['description2']}
                </p>
            </div>

            <div class="descriptions_ctnr descriptions_ctnr_alt2">
                <p class="service_heading">
                    {service_dict['heading2']}
                </p>
                <p>
                    {service_dict['description3']}
                </p>
                <p>
                    {service_dict['description4']}
                </p>
            </div>


            <div class="ul_ctnr">
                <p class="service_heading">
                    {service_dict['ul1_heading']}
                </p>
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
                    <li>
                        {service_dict['ul1_li5']}
                    </li>
                    <li>
                        {service_dict['ul1_li6']}
                    </li>
                </ul>
`                <p>
                    {service_dict['ul1_footer']}
                </p>
`            </div>

            <p class="service_heading">
                {service_dict['heading4']}
            </p>

            <div class="ul_ctnr">
                <p class="service_heading">
                    {service_dict['ul2_heading']}
                </p>
                <ul>
                    <li>
                        {service_dict['ul2_li1']}
                    </li>
                    <li>
                        {service_dict['ul2_li2']}
                    </li>
                    <li>
                        {service_dict['ul2_li3']}
                    </li>
                    <li>
                        {service_dict['ul2_li4']}
                    </li>
                    <li>
                        {service_dict['ul2_li5']}
                    </li>
                </ul>
            </div>

            <p class="service_heading">
                {service_dict['heading5']}
            </p>

            <div class="descriptions_ctnr">
                <p>
                    {service_dict['description5']}
                </p>
                <p>
                    {service_dict['description6']}
                </p>
            </div>
        </div>
    </div>
</div>
    """)