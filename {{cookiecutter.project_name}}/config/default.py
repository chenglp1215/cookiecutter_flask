import os

from config.common import Config, basedir


class FullConfig(Config):
    def __init__(self):
        pass

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-default.sqlite')

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    WX_LOG_FILE = 'wxlog.log'

    UPLOAD_FOLDER = os.path.join(basedir, 'uploads')
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'zip'}

    UPLOAD_LOG = '/tmp/upload_log.log'
    REMOTE_UPLOAD_PATH = '/tmp'
