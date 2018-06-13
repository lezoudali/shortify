from .exceptions import IntegrityError
from .abstract import AbstractDBStorage


class RedisStorage(AbstractDBStorage):
    def __init__(self, connection):
        self._conn = connection

    def insert(self, key, value, overwrite=False):
        if (not overwrite):
            self._exists_or_raise(key)
        self._conn.append(key, value)

    def get(self, key):
        return self._conn.get(key)

    def exists(self, key):
        return self._conn.exists(key)

    def delete_all(self):
        self._conn.flushdb()

    def size(self):
        return self._conn.dbsize()

    def _exists_or_raise(self, key):
        if self._conn.exists(key):
            raise IntegrityError(f"{key} already exists.")
