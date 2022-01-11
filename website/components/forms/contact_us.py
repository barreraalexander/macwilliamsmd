from flask import Markup, url_for

from website.components.parts.button_like import component as button_like
from website.blueprints.api.forms import ContactUsForm

def component():
    form = ContactUsForm()
    action = url_for('api.send_contact')
    send_img_src = url_for('static', filename='images/assets/send.svg')
    return Markup(f"""
    <form
        id="contact_form"
        action="{action}"
        method="POST"
    >
        {form.hidden_tag()}
        <div class="form_columns">
            <div class="form_column">
                <div class="form_group">
                    {form.fname.label}
                    {form.fname}
                </div>
                <div class="form_group">
                    {form.fname.label}
                    {form.fname}
                </div>
            </div>
            <div class="form_column">
                <div class="form_group">
                    {form.fname.label}
                    {form.fname}
                </div>
                <div class="form_group">
                    {form.fname.label}
                    {form.fname}
                </div>
            </div>

            <div class="recaptcha_ctnr">
            </div>


            <div class="form_group_btn_lg">
                {button_like('submit', elem_id='contact_submit')}
                {form.submit}
            </div>

            <div class="form_group_btn">
                <img
                    src="{send_img_src}"
                    alt="send icon"
                >
            </div>
        
        </div>
    </form>



    """)