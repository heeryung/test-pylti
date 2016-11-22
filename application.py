import os
from flask import Flask
from flask import render_template
from flask.ext.wtf import Form
from wtforms import IntegerField, BooleanField, StringField, RadioField, SubmitField
from wtforms.validators import Required
from random import randint
from pylti.flask import lti

VERSION = '0.0.1'

# EB looks for an 'app' callable by default.
application = Flask(__name__)
app = application
app.config.from_object('config')

# # add a rule for the index page.
# app.add_url_rule('/', 'index', (lambda: header_text +
#     say_hello() + instructions + footer_text))

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


@app.route('/is_up', methods=['GET'])
def is_up(lti=lti):
    """ Indicate the app is working. Provided for debugging purposes.

    :param lti: the `lti` object from `pylti`
    :return: simple page that indicates the request was processed by the lti
        provider
    """
    return render_template('up.html', lti=lti)


@app.route('/', methods=['GET', 'POST'])
@lti(request='initial', error=error, app=app)
def redirect_to(lti=lti) :
    return render_template('index.html', lti=lti)

# @app.route('/lti/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
# @lti(request='any', error=error, app=app)
def index(lti=lti):
    """ initial access page to the lti provider.  This page provides
    authorization for the user.

    :param lti: the `lti` object from `pylti`
    :return: index page for lti provider
    """
    return render_template('index.html', lti=lti)


@app.route('/index_staff', methods=['GET', 'POST'])
@lti(request='session', error=error, role='staff', app=app)
def index_staff(lti=lti):
    """ render the contents of the staff.html template

    :param lti: the `lti` object from `pylti`
    :return: the staff.html template rendered
    """
    return render_template('staff.html', lti=lti)


@app.route('/add', methods  =['GET', 'POST'])
# @lti(request = "session", error=error, app=app)
def add_form(lti=lti):
    """ initial access page for lti consumer

    :param lti: the `lti` object from `pylti`
    :return: index page for lti provider
    """
    form = AddForm()
    form.id_subject.data = randint(1, 9)
    form.gender.data = randint(1, 9)
    return render_template('add.html', form=form)


@app.route('/grade', methods=['POST'])
@lti(request='session', error=error, app=app)
def grade(lti=lti):
    """ post grade

    :param lti: the `lti` object from `pylti`
    :return: grade rendered by grade.html template
    """
    form = AddForm()
    correct = ((form.p1.data + form.p2.data) == form.result.data)
    form.correct.data = correct
    lti.post_grade(1 if correct else 0)
    return render_template('grade.html', form=form)


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
    port = int(os.environ.get("FLASK_LTI_PORT", 5000))
    host = os.environ.get("FLASK_LTI_HOST", "localhost")
    app.run(debug=True, host=host, port=port)
