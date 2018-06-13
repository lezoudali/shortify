from flask import jsonify
from werkzeug.exceptions import HTTPException


def abort(message, status_code, headers=None):
    response = jsonify({'error': message})
    response.status_code = status_code
    response.headers = headers or {}
    response.headers['Content-Type'] = 'application/json'

    return HTTPException(description=None, response=response)


def bad_request(message=None):
    status_code = 404

    return abort(message, status_code)
