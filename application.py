import os
from flask import Flask
from flask import render_template
from flask_wtf import Form
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import Required
from random import randint
from pylti.flask import lti

# https://3v2m94ybq4.execute-api.us-east-1.amazonaws.com/dev/index`

VERSION = '0.0.1'

application = Flask(__name__)
application.config.from_object('config')


class AddForm(Form):

    id_subject = StringField('ID', validators= [Required()])
    gender = RadioField("Gender",
        choices=[('m', "male"), ('f', "female"), ('o', "other")],
        validators=[Required()], default=None)
    submit = SubmitField('Submit')



def error(exception):
    """ render error page

    :param exception: optional exception
    :return: the error.html template rendered
    """
    return render_template('error.html')


@application.route('/is_up')
def is_up(lti=lti):
    """ Indicate the app is working. Provided for debugging purposes.

    :param lti: the `lti` object from `pylti`
    :return: simple page that indicates the request was processed by the lti
        provider
    """
    return render_template('up.html', lti=lti)



@application.route('/index', methods=['GET', 'POST'])
@lti(request='initial', error=error, application=application)
# @lti(request='any', error=error, application=application)
def redirect_to(lti=lti) :
    # We can match people
    return render_template('index.html', lti=lti)




@application.route('/add')
@lti(request = "session", error=error, application=application)
def add_form(lti=lti):
    """ initial access page for lti consumer

    :param lti: the `lti` object from `pylti`
    :return: index page for lti provider
    """
    form = AddForm()
    form.id_subject.data = randint(1, 9)
    form.gender.data = randint(1, 9)
    return render_template('add.html', form=form)




def set_debugging():
    """ enable debug logging

    """
    import logging
    import sys

    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(name)s - %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)

set_debugging()

if __name__ == '__main__':
    """
    For if you want to run the flask development server
    directly
    """
    port = int(os.environ.get("PORT", 5000))
    host = os.environ.get("FLASK_LTI_HOST", "localhost")
    application.run(debug=True, host=host, port=port)
