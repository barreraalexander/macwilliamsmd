from flask import Blueprint, render_template, url_for
import json


api = Blueprint ('api', __name__ )

@api.route('/', methods=['GET', 'POST'])
def index():
    return 'hey'