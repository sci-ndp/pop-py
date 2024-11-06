import pytest
from unittest.mock import patch, MagicMock
from pointofpresence.get_method import APIClientGet


@pytest.fixture
def client():
    """Fixture for APIClientGet without triggering network calls."""
    with patch.object(APIClientGet, "_check_api_availability"):
        return APIClientGet(base_url="https://api.example.com")


@patch("pointofpresence.client_base.requests.Session.get")
@patch.object(APIClientGet, "_check_api_availability")
def test_get(mock_check_api, mock_get, client):
    """Test the GET method."""
    mock_check_api.return_value = None

    # Mock the GET response
    mock_response = MagicMock()
    mock_response.json.return_value = {"result": "success"}
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    # Call the get method on the client
    response = client.get("/endpoint")

    # Assertions to verify correct behavior
    assert response == {"result": "success"}  # Check the returned data
    mock_get.assert_called_once_with(
        "https://api.example.com/endpoint", params=None
    )
