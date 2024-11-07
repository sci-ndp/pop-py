from .client_base import APIClientBase
from requests.exceptions import HTTPError


class APIClientSearch(APIClientBase):
    """
    Extension of APIClientBase with search functionality for data sources.
    """

    def search(
        self,
        dataset_name=None,
        dataset_title=None,
        owner_org=None,
        resource_url=None,
        resource_name=None,
        dataset_description=None,
        resource_description=None,
        resource_format=None,
        search_term=None,
        timestamp=None,
        server="local",
    ):
        """
        Search for data sources by various parameters.

        :param dataset_name: The name of the dataset.
        :param dataset_title: The title of the dataset.
        :param owner_org: The organization owning the dataset.
        :param resource_url: URL of the resource.
        :param resource_name: Name of the resource.
        :param dataset_description: Description of the dataset.
        :param resource_description: Description of the resource.
        :param resource_format: Format of the resource (e.g., CSV, JSON).
        :param search_term: Search term to apply across all fields.
        :param timestamp: Time range for filtering results.
        :param server: 'local' or 'global' server selection.
        :return: List of matching datasets.
        :raises ValueError: If the search fails.
        """
        url = f"{self.base_url}/search"
        params = {
            "dataset_name": dataset_name,
            "dataset_title": dataset_title,
            "owner_org": owner_org,
            "resource_url": resource_url,
            "resource_name": resource_name,
            "dataset_description": dataset_description,
            "resource_description": resource_description,
            "resource_format": (
                resource_format.lower() if resource_format else None
            ),
            "search_term": search_term,
            "timestamp": timestamp,
            "server": server,
        }

        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except HTTPError as e:
            error_detail = response.json().get("detail", str(e))
            raise ValueError(
                f"Error searching for data sources: {error_detail}"
            )
