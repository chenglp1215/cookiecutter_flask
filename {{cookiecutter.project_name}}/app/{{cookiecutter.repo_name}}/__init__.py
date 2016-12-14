from flask import Blueprint

{{cookiecutter.repo_name}} = Blueprint("{{cookiecutter.repo_name}}", __name__)

from . import views, errors
