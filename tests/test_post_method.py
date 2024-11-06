import pytest
from unittest.mock import patch, MagicMock
from pointofpresence.post_method import APIClientPost


@pytest.fixture
def client():
    """Fixture for APIClientPost without triggering network calls."""
    with patch.object(APIClientPost, "_check_api_availability"):
        return APIClientPost(base_url="https://api.example.com")


@patch("pointofpresence.client_base.requests.Session.post")
@patch.object(APIClientPost, "_check_api_availability")
def test_post(mock_check_api, mock_post, client):
    """Test the POST method."""
    mock_check_api.return_value = None

    # Mock the POST response
    mock_response = MagicMock()
    mock_response.json.return_value = {"result": "success"}
    mock_response.status_code = 201
    mock_post.return_value = mock_response

    # Call the post method on the client
    data = {"key": "value"}
    response = client.post("/endpoint", data=data)

    # Assertions to verify correct behavior
    assert response == {"result": "success"}  # Directly check the dictionary
    mock_post.assert_called_once_with(
        "https://api.example.com/endpoint", json=data
    )
