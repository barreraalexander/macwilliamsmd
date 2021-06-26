from flask import Blueprint, render_template, url_for
from website.blueprints.main import BUSINESS_INFO


main = Blueprint ('main', __name__ )

@main.route('/home')
@main.route('/')
def index():
    title="Home"
    return render_template('_index.html',
                            title=title)

@main.route('/services')
def services():
    title="Services"
    return render_template('_services.html',
                            title=title)


@main.route('/new_patient')
def new_patient():
    title="new_patient"
    return render_template('_new_patient.html',
                            title=title)

@main.route('/doctors')
def doctors():
    title="doctors"
    return render_template('_doctors.html',
                            title=title)

@main.route('/contact')
def contact():
    title="contact"
    return render_template('_contact.html',
                            title=title)

@main.route('/about')
def about():
    title="about"
    return render_template('_about.html',
                            title=title)


