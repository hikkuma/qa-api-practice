import pytest
import requests


@pytest.fixture
def api_session():
    session = requests.Session()
    session.base_url = "https://jsonplaceholder.typicode.com"
    yield session
    session.close()
