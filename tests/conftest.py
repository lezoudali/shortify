import pytest
from shortify.db import create_db


@pytest.fixture(scope='session')
def db():
    storage = create_db(host='localhost', db=1)

    yield storage

    storage.delete_all()
