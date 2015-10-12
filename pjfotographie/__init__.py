from flask import Flask, flash, render_template
from views.pages import simple_page
from views.contact_form import ContactForm

app = Flask(__name__)
app.config.from_object('config.ProductionConfig')

# A blueprint to render all pages.
app.register_blueprint(simple_page)


@app.route('/contact/', methods=['POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash("Thanks for your note. I will reach out to you shortly.",
              "success")
        return render_template('contact.html', form=form)
    flash("Please re-submit the form again.",
          "errors")
    return render_template('contact.html', form=form)
