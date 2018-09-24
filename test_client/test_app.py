import pytest

from app import app, db


@pytest.fixture
def client():
    app.config['TESTING'] = True
    db.create_all()
    yield app.test_client()


def test_get_pets_on_empty_db(client):
    result = client.get('/pets')
    assert result.status_code == 200
    assert result.json == []


def test_put_pet(client):
    # TODO: Pet creation scenario
    pass


if __name__ == "__main__":
    pytest.main()
