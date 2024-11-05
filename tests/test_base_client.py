import pytest
from pointofpresence.client_base import APIClientBase


@pytest.fixture
def client():
    return APIClientBase(base_url='https://api.example.com')

def test_get_token(client):
    """Test the get_token method."""
    # Implement your test logic here
    pass
