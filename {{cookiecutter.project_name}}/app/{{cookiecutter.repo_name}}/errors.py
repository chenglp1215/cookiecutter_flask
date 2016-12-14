from . import {{cookiecutter.repo_name}}


@{{cookiecutter.repo_name}}.app_errorhandler(404)
def page_not_found(e):
    return "<h1>Page Not Found</h1>"


@{{cookiecutter.repo_name}}.app_errorhandler(500)
def internal_server_error(e):
    return "<h1>Internal Server Error</h1>"

