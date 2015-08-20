from flask import Flask, render_template
from views.pages import simple_page

app = Flask(__name__)
app.config.from_object('config.ProductionConfig')

# A blueprint to render all pages.
app.register_blueprint(simple_page)