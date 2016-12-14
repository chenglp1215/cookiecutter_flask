from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


from config import config

db = SQLAlchemy()
bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

    config[config_name].init_app(app)

    db.init_app(app)
    bootstrap.init_app(app)

    from .{{cookiecutter.repo_name}} import {{cookiecutter.repo_name}} as {{cookiecutter.repo_name}}_blueprint
    app.register_blueprint({{cookiecutter.repo_name}}_blueprint)

    return app

