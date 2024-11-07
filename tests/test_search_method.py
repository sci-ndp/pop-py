import pytest
from unittest.mock import patch, MagicMock
from pointofpresence.search_method import APIClientSearch
from requests.exceptions import HTTPError


@pytest.fixture
def client():
    """Fixture for APIClientSearch without triggering network calls."""
    with patch.object(APIClientSearch, "_check_api_availability"):
        return APIClientSearch(base_url="https://api.example.com")


def test_search_success(client):
    """Test the search method with successful search."""
    with patch("pointofpresence.client_base.requests.Session.get") as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"id": "123", "name": "example_dataset", "title": "Example Title"}
        ]
        mock_get.return_value = mock_response

        response = client.search(dataset_name="example_dataset")
        assert response == [
            {"id": "123", "name": "example_dataset", "title": "Example Title"}
        ]

        mock_get.assert_called_once_with(
            "https://api.example.com/search",
            params={
                "dataset_name": "example_dataset",
                "dataset_title": None,
                "owner_org": None,
                "resource_url": None,
                "resource_name": None,
                "dataset_description": None,
                "resource_description": None,
                "resource_format": None,
                "search_term": None,
                "timestamp": None,
                "server": "local",
            },
        )


def test_search_no_results(client):
    """Test the search method with no results found."""
    with patch("pointofpresence.client_base.requests.Session.get") as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = []
        mock_get.return_value = mock_response

        response = client.search(dataset_name="nonexistent_dataset")
        assert response == []

        mock_get.assert_called_once_with(
            "https://api.example.com/search",
            params={
                "dataset_name": "nonexistent_dataset",
                "dataset_title": None,
                "owner_org": None,
                "resource_url": None,
                "resource_name": None,
                "dataset_description": None,
                "resource_description": None,
                "resource_format": None,
                "search_term": None,
                "timestamp": None,
                "server": "local",
            },
        )


def test_search_http_error(client):
    """Test the search method with an HTTP error."""
    with patch("pointofpresence.client_base.requests.Session.get") as mock_get:
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = HTTPError("HTTP Error")
        mock_get.return_value = mock_response

        with pytest.raises(ValueError) as exc_info:
            client.search(dataset_name="error_dataset")

        assert "Error searching for data sources" in str(exc_info.value)

        mock_get.assert_called_once_with(
            "https://api.example.com/search",
            params={
                "dataset_name": "error_dataset",
                "dataset_title": None,
                "owner_org": None,
                "resource_url": None,
                "resource_name": None,
                "dataset_description": None,
                "resource_description": None,
                "resource_format": None,
                "search_term": None,
                "timestamp": None,
                "server": "local",
            },
        )


def test_search_specific_filter(client):
    """Test the search method with a specific filter."""
    with patch("pointofpresence.client_base.requests.Session.get") as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                "id": "456",
                "name": "filtered_dataset",
                "title": "Filtered Title",
            }
        ]
        mock_get.return_value = mock_response

        response = client.search(dataset_title="Filtered Title")
        assert response == [
            {
                "id": "456",
                "name": "filtered_dataset",
                "title": "Filtered Title",
            }
        ]

        mock_get.assert_called_once_with(
            "https://api.example.com/search",
            params={
                "dataset_name": None,
                "dataset_title": "Filtered Title",
                "owner_org": None,
                "resource_url": None,
                "resource_name": None,
                "dataset_description": None,
                "resource_description": None,
                "resource_format": None,
                "search_term": None,
                "timestamp": None,
                "server": "local",
            },
        )
