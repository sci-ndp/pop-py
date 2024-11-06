import pytest
from unittest.mock import patch, MagicMock
from pointofpresence.delete_method import APIClientDelete


@pytest.fixture
def client():
    """Fixture for APIClientDelete without triggering network calls."""
    with patch.object(APIClientDelete, "_check_api_availability"):
        return APIClientDelete(base_url="https://api.example.com")


@patch("pointofpresence.client_base.requests.Session.delete")
@patch.object(APIClientDelete, "_check_api_availability")
def test_delete(mock_check_api, mock_delete, client):
    """Test the DELETE method."""
    mock_check_api.return_value = None

    # Mock the DELETE response
    mock_response = MagicMock()
    # 204 No Content is typical for successful DELETE
    mock_response.status_code = 204
    mock_delete.return_value = mock_response

    # Call the delete method on the client
    response = client.delete("/endpoint")

    # Assertions to verify correct behavior
    # Check that the response matches the status code directly
    assert response == 204
    mock_delete.assert_called_once_with("https://api.example.com/endpoint")
