import os
import redis
from .storage import RedisStorage


def default_connection_options():
    return dict(
        host=os.getenv('SHORTIFY_REDIS_HOST', 'localhost'),
        port=os.getenv('SHORTIFY_REDIS_PORT', 6379),
        db=os.getenv('SHORTIFY_REDIS_DB', 0),
        charset='utf-8',
        decode_responses=True,
    )

def create_connection(options=None):
    assert isinstance(options, (dict, type(None)))

    options = options or default_connection_options()
    return redis.StrictRedis(**options)


def create_storage(**connection_options):
    options = {**default_connection_options(), **connection_options}
    conn = create_connection(options)

    return RedisStorage(conn)
