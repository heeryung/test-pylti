"""
Configuration file for flask sample application
"""
import os


# enable CSRF
WTF_CSRF_ENABLED = True

# secret key for authentication
SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "heeryung_test_flask_secret")
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

