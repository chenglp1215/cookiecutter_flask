import os

from config.common import Config, basedir


class FullConfig(Config):
    def __init__(self):
        pass

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'mysql://root:csly@127.0.0.1:3306/firstflask'

    WX_LOG_FILE = '/tmp/wxlog.log'