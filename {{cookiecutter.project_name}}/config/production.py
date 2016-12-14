import os

from config.common import Config, basedir


class FullConfig(Config):
    def __init__(self):
        pass

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('PRO_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-pro.sqlite')

    UPLOAD_FOLDER = os.path.join(basedir, 'uploads')
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'zip', 'mp4', 'avi', 'flv'}
    UPLOAD_LOG = '/tmp/upload_log.log'
    REMOTE_UPLOAD_PATH = '/tmp'
