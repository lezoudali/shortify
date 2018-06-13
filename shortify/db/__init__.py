import os
import redis

from .redis_storage import RedisStorage
from .exceptions import IntegrityError   # flake8: noqa


def default_connection_options():
    return dict(
        host=os.getenv('SHORTIFY_REDIS_HOST', 'localhost'),
        port=os.getenv('SHORTIFY_REDIS_PORT', 6379),
        db=os.getenv('SHORTIFY_REDIS_DB', 0),
        charset='utf-8',
        decode_responses=True,
    )


def create_db(**connection_options):
    options = {**default_connection_options(), **connection_options}

    conn = redis.StrictRedis(**options)

    return RedisStorage(conn)
