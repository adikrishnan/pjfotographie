from sparkpost import SparkPost, SparkPostException
from jinja2 import Environment, PackageLoader
from pjfotographie import app


def send_email(body):
    try:
        sp = SparkPost()
        from_email = app.config.get('FROM_EMAIL')
        response = sp.transmission.send(
            recipients=[app.config.get('RECIPIENT_EMAIL')],
            text=body,
            from_email=from_email,
            subject='A New Message on Patrick Joseph Photography Website'
        )
        app.logger.info(response)
        if response.get('total_accepted_recipients') == 1:
            return True
        else:
            app.logger.warning(response.get('total_accepted_recipients'))
            return False
    except SparkPostException as ex:
        app.logger.error(ex)
        return False


def update_body(name, email_address, contact_number, message=None):
    env = Environment(loader=PackageLoader('pjfotographie', 'templates'))
    template = env.get_template('email_template.j2')
    body = template.render(name=name,
                           email_address=email_address,
                           contact_number=contact_number,
                           message=message)
    result = send_email(body)
    return result
