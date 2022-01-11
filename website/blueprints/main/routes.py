from flask import Blueprint, render_template, url_for
from website import cache

from website.blueprints.main import CONTACT_DICT, SERVICES, META_DICT
from website.components.parts.button_like import component as button_like

# navbars
from website.components.navbars.linkset import component as linkset
from website.components.navbars.header import component as header
from website.components.navbars.footer import component as footer

# sections
from website.components.sections.hero import component as hero_section
from website.components.sections.about import component as about_section
from website.components.sections.services import component as services_section

# components
from website.components.parts.doctor_panel import component as doctor_panel

#  forms
from website.components.forms.contact_us import component as contact_us_form

main = Blueprint ('main', __name__ )

@main.context_processor
def load_dicts():
    return dict(
        CONTACT_DICT=CONTACT_DICT,
        META_DICT=META_DICT,
        SERVICES=SERVICES
    )

@main.context_processor
def load_base():
    return dict(
        header=header,
        footer=footer,
        linkset=linkset,
    )

@main.context_processor
def load_components():
    return dict(
        button_like=button_like,
    )



@main.route('/home')
@main.route('/')
# @cache.cached(timeout=0)
def index():
    return render_template('_index.html',
        title="Home",
        hero_section=hero_section,
        )


@main.route('/about')
def about():
    return render_template('_about.html',
        title="About Us",
        about_section=about_section,
        )


@main.route('/doctors')
def doctors():
    
    return render_template('_doctors.html',
        title="Our Doctors",
        doctor_panel=doctor_panel,
        )


@main.route('/services')
def services():
    return render_template('_services.html',
        title="Our Services",
        services_section=services_section,
        )

@main.route('/contact')
def contact():
    return render_template('_contact.html',
        title="Contact",
        contact_us_form=contact_us_form,
        )


@main.route('/sitemap')
def sitemap():
    return render_template('_sitemap.html',
        title="Sitemap",
        )