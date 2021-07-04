from flask import Blueprint, render_template, url_for
from website.blueprints.main import CONTACT_DICT
from website.components.button_like import component as button_like
from website.components.doctor_card import component as doctor_card
from website.components.doctor_panel import component as doctor_panel
from website.components.service_panel import component as service_panel
from website.components.service_slide import component as service_slide
from website.components.doctor_card import component as doctor_card
from website.blueprints.api.forms import ContactUsForm
from website.blueprints.api.forms import NewClientForm

main = Blueprint ('main', __name__ )

@main.route('/home')
@main.route('/')
def index():
    return render_template('_index.html',
                        title="Home",
                        button_like=button_like,
                        service_slide=service_slide,
                        doctor_card=doctor_card,
                        CONTACT_DICT=CONTACT_DICT)


@main.route('/about')
def about():
    return render_template('_about.html',
                        title="About Us",
                        button_like=button_like,
                        CONTACT_DICT=CONTACT_DICT)


@main.route('/doctors')
def doctors():
    return render_template('_doctors.html',
                        title="Our Doctors",
                        button_like=button_like,
                        doctor_panel=doctor_panel,
                        CONTACT_DICT=CONTACT_DICT)


@main.route('/services')
def services():
    return render_template('_services.html',
                        title="Our Services",
                        button_like=button_like,
                        service_panel=service_panel,
                        CONTACT_DICT=CONTACT_DICT)

@main.route('/contact')
def contact():
    form = ContactUsForm()
    return render_template('_contact.html',
                        title="Contact",
                        button_like=button_like,
                        service_panel=service_panel,
                        form=form,
                        CONTACT_DICT=CONTACT_DICT)


@main.route('/new_client')
def new_client():
    form = NewClientForm()
    return render_template('_new_client.html',
                        title="New Client",
                        button_like=button_like,
                        service_panel=service_panel,
                        form=form,
                        CONTACT_DICT=CONTACT_DICT)

