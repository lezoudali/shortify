import pytest
from shortify.db.redis_storage import create_storage


@pytest.fixture(scope='session')
def storage():
    storage = create_storage(host='localhost', port=8000, db=1)

    yield storage

    storage.connection.flushdb()
    storage.connection.shutdown()
