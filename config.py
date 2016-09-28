"""
Configuration file for flask sample application
"""
import os


# enable CSRF
WTF_CSRF_ENABLED = True

# secret key for authentication
SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "heeryung_test_flask_secret")

# Sample client certificate example for 12 factor app
# You would want to store your entire pem in an environment variable
# with something like:
# ```
# export CONSUMER_KEY_CERT=$(cat <<EOF
# < paste cert here>
# EOF
# )
# ```

CONSUMER_KEY_PEM_FILE = os.path.abspath('consumer_key.pem')
with open(CONSUMER_KEY_PEM_FILE, 'w') as wfile:
    wfile.write(os.environ.get('CONSUMER_KEY_CERT', ''))

PYLTI_CONFIG = {
    "consumers": {
        "heeryung_test_consumer_key": {
            "secret": os.environ.get("CONSUMER_KEY_SECRET", "heeryung_test_consumer_secret"),
            "cert": CONSUMER_KEY_PEM_FILE
        }
    }
}

# Remap URL to fix edX's misrepresentation of https protocol.
# You can add another dict entry if you have trouble with the
# PyLti URL.
PYLTI_URL_FIX = {
    "https://localhost:8000/": {
        "https://localhost:8000/": "http://localhost:8000/"
    },
    "https://localhost/": {
        "https://localhost/": "http://192.168.33.10/"
    }
}
