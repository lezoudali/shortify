from flask import current_app as app, redirect, request, jsonify
from webargs import fields
from webargs.flaskparser import use_args

from shortify.slug_generator import random_slug_generator
from shortify import http_utils as http

shortify_args = {
    'destination': fields.Str(required=True),
}


@use_args(shortify_args)
def shortify(args):
    slug = _generate_unique_slug()
    destination = args.get('destination')

    app.db.insert(slug, destination)

    return jsonify({
        'slug': slug,
        'destination': destination
    })


def welcome():
    return 'welcome to shortify'


def redirect_to_dest(path):
    path = request.path[1:]
    destination = app.db.get(path)
    if destination:
        if (not destination.startswith('http://') and
                not destination.startswith('https://')):
            destination = f"http://{destination}"
        return redirect(destination)

    return http.bad_request('invalid short link')


def _generate_unique_slug():
    slug = random_slug_generator()
    while app.db.exists(slug):
        slug = random_slug_generator()
    return slug


resources = {
    shortify: ('/api/shortify', ['POST'], {}),
    redirect_to_dest: ('/<path:path>', ['GET'], {}),
    welcome: ('/', ['GET'], {}),
}
