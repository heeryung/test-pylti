from pylti.flask import lti

app = Flask(__name__)


@app.route("/any")
@lti(error=error, request='any', app=app)
def any_route(lti):
    """
    In this example route /any is protected and initial or subsequent calls
    to the URL will succeed. As you can see lti passed one keyword parameter
    lti object that can be used to inspect LTI session.

    :param: lti: `lti` object
    :return: string "html to return"
    """
    return "Landing page"
