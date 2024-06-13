import os


class Config(object):
    # reCAPTCHA configuration
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")