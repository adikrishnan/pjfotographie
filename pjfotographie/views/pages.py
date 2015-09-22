from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simple_page = Blueprint('simple_page', __name__, template_folder='templates')


@simple_page.route('/', defaults={'page': 'home'})
@simple_page.route('/<page>/')
def show(page):
    try:
        if page.find('my-art') != -1:
            return render_template('my-art.html')
        return render_template('%s.html' % page)
    except TemplateNotFound:
        abort(404)
