from flask import Flask, flash, render_template, request
from os import environ

app = Flask(__name__)
app.config.from_object('config.ProductionConfig')
app.config.update(environ)

from pjfotographie.views.pages import simple_page
from pjfotographie.views.contact_form import ContactForm
from pjfotographie.utils.send_email import update_body

# A blueprint to render all pages.
app.register_blueprint(simple_page)


@app.route('/contact/', methods=['POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        result = update_body(name, email, phone, message)
        if result:
            flash("Thanks for your note. I will reach out to you shortly.",
                  "success")
            return render_template('contact.html', form=form)
        else:
            flash("I was unable to get your message. Please reach out\
                  to me at patrickjosephphotography@gmail.com",
                  "errors")
            return render_template('contact.html', form=form)
    flash("The form had errors. Please re-submit the form again.",
          "errors")
    return render_template('contact.html', form=form)
