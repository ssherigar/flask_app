import pytest

from app import app

@pytest.fixture
def client():
    """ Create and configure a new app instance for each test."""
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

