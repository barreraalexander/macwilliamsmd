from flask import Blueprint, render_template, url_for
from website.blueprints.main import CONTACT_DICT, SERVICES, META_DICT

from website.blueprints.api.forms import ContactUsForm

from website.components.button_like import component as button_like
from website.components.doctor_card import component as doctor_card
from website.components.doctor_panel import component as doctor_panel
from website.components.doctor_panel_lg import component as doctor_panel_lg
from website.components.service_panel import component as service_panel
from website.components.service_slide import component as service_slide
from website.components.slide_text import component as slide_text
from website.components.service_grid import component as service_grid
from website.components.doctor_card import component as doctor_card
from website.components.navbars.linkset import component as linkset
from website.components.navbars.header import component as header
from website.components.navbars.footer import component as footer



main = Blueprint ('main', __name__ )

@main.context_processor
def load_dicts():
    return dict(
        CONTACT_DICT=CONTACT_DICT,
        META_DICT=META_DICT,
        SERVICES=SERVICES
    )


@main.context_processor
def load_components():
    return dict(
        button_like=button_like,
        service_slide=service_slide,
        doctor_card=doctor_card,
        doctor_panel=doctor_panel,
        service_panel=service_panel,
        service_grid=service_grid,
        doctor_panel_lg=doctor_panel_lg,
        slide_text=slide_text,
        header=header,
        footer=footer
    )



@main.route('/home')
@main.route('/')
def index():
    return render_template('_index.html',
                        title="Home")


@main.route('/about')
def about():
    return render_template('_about.html',
                        title="About Us")


@main.route('/doctors')
def doctors():
    return render_template('_doctors.html',
                        title="Our Doctors")


@main.route('/services')
def services():
    return render_template('_services.html',
                        title="Our Services")

@main.route('/contact')
def contact():
    form = ContactUsForm()
    return render_template('_contact.html',
                        form=form,
                        title="Contact")


@main.route('/sitemap')
def sitemap():
    return render_template('_sitemap.html',
                        title="Sitemap")
    


# @main.route('/new_client')
# def new_client():
#     form = NewClientForm()
#     return render_template('_new_client.html',
#                         title="New Client",
#                         button_like=button_like,
#                         service_panel=service_panel,
#                         form=form,
#                         link_set=link_set,
#                         service_grid=service_grid,
                        # META_DICT=META_DICT,
#                         CONTACT_DICT=CONTACT_DICT)

