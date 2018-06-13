from flask import Flask
from webargs.flaskparser import parser

from shortify.db import create_db
from shortify import http_utils as http
from shortify.api import resources as api_resources


class ShortifyApp(Flask):
    def __init__(self, *args, db=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.db = db


def create_app():
    db = create_db()
    app = ShortifyApp(__name__, db=db)

    register_error_handlers(app)
    init_api(app)

    return app


def init_api(app):
    for view_func, route_rules in api_resources.items():
        route, methods, options = route_rules
        app.add_url_rule(route, view_func=view_func,
                         methods=methods, **options)


def register_error_handlers(app):
    @parser.error_handler
    def handle_webargs_error(err):
        return http.abort(err.messages, 422)

    @app.errorhandler(404)
    @app.errorhandler(500)
    @app.errorhandler(400)
    def handle_http_error(err):
        return http.abort(str(err), getattr(err, 'code', 400))
