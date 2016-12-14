# coding=utf-8

from flask import request, render_template, session, abort, make_response

from . import {{cookiecutter.repo_name}}
from .errors import page_not_found


@{{cookiecutter.repo_name}}.route(r'/', methods=['GET', "POST"])
def index():
    if request.method == 'GET':
        return make_response("hello flask")
    else:
        abort(404)

