from flask import Blueprint, render_template
from website.blueprints.main import META_DICT, CONTACT_DICT
from website.components.navbars.linkset import component as linkset
from website.components.parts.button_like import component as button_like

errors = Blueprint ('errors', __name__)


errors.context_processor
def load_base():
    return dict(
        META_DICT=META_DICT,
        CONTACT_DICT=CONTACT_DICT,
        linkset=linkset,
    )

errors.context_processor
def load_components():
    return dict(
        button_like=button_like,
    )


@errors.app_errorhandler(404)
def error_404(error):
    error_code = "404"
    error_text = "Sorry, but this page doesn't exist. Please go back. "
    return render_template('errors/error.html',
        title='404 Error',
        error_code=error_code,
        error_text=error_text,
        ), 404


@errors.app_errorhandler(403)
def error_403(error):
    error_code = "403"
    error_text = """
                Sorry, but you're trying to reach a page
                that you're not supposed to have access to.
                Please go back. 
                """
    return render_template('errors/403.html',
        title='403 Error',
        error_text=error_text,
        error_code=error_code,
        ), 403

@errors.app_errorhandler(500)
def error_500(error):
    error_code = "500"
    error_text = f"""
                Oh boy. There's something wrong with our
                server. Please give us a call at
                {CONTACT_DICT['phone']}.
                """
    return render_template('errors/500.html',
        title='500 Error',
        error_text=error_text,
        error_code=error_code
        ), 500

