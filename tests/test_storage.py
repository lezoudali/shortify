import pytest

from shortify.db import IntegrityError


def test_should_successfully_insert(db):
    db.insert('ping', 'pong')

    assert db.exists('ping')


def test_should_retrieve_inserted_data(db):
    db.insert('hello', 'world')

    assert db.get('hello') == 'world'


def test_should_raise_if_key_exists(db):
    db.insert('john', 'doe')

    with pytest.raises(IntegrityError) as exc:
        db.insert('john', 'Doe')

    exc_msg = str(exc.value)

    assert 'john already exists.' == exc_msg


def test_should_return_size(db):
    db.insert('lebron', 'james')

    assert db.size() >= 1

    db.delete_all()

    assert db.size() == 0
