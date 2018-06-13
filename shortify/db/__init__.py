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
    get_options = lambda: {**default_connection_options(), **connection_options}
    redis_url = os.getenv('REDIS_URL')


    conn = (redis.StrictRedis.from_url(
                redis_url,
                decode_responses=True,
                charset='utf-8'
            ) if redis_url
            else redis.StrictRedis(**get_options()))

    return RedisStorage(conn)
