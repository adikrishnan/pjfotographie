import os

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from contact_form import ContactForm
from pjfotographie import app
from pjfotographie.utils.os_utils import fetch_all_files

simple_page = Blueprint('simple_page', __name__, template_folder='templates')


@simple_page.route('/', defaults={'page': 'home'})
@simple_page.route('/<page>/')
def show(page):
    try:
        if page == 'contact':
            form = ContactForm()
            return render_template('contact.html', form=form)
        if page == 'wedding':
            rel_path = app.config.get('WEDDING_THUMBNAILS_DIR')
            img_list = fetch_all_files(rel_path)
            return render_template('wedding.html', thumbnail_images=img_list)
        if page == 'myart':
            rel_path = app.config.get('ASSORTED_THUMBNAILS_DIR')
            img_list = fetch_all_files(rel_path)
            return render_template('myart.html', thumbnail_images=img_list)
        return render_template('%s.html' % page)
    except TemplateNotFound as ex:
        app.logger.error(ex)
        abort(404)
