from flask import Blueprint, render_template, url_for
from website.blueprints.main import CONTACT_DICT
from website.components.button_like import component as button_like

main = Blueprint ('main', __name__ )

@main.route('/')
def index():
    return render_template('_index.html',
                        button_like=button_like,
                        CONTACT_DICT=CONTACT_DICT)

