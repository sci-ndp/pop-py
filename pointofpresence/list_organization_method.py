# pointofpresence/list_organization_method.py

from .client_base import APIClientBase
from requests.exceptions import HTTPError


class APIClientOrganizationList(APIClientBase):
    """Extension of APIClientBase with method to list organizations."""

    def list_organizations(self, name=None, server="global"):
        """
        List all organizations, with optional name filtering and server
        selection.

        :param name: Optional string to filter organizations by name.
        :param server: The CKAN server to query ('local', 'global',
        'pre_ckan').
        :return: List of organization names.
        :raises ValueError: If the retrieval fails.
        """
        url = f"{self.base_url}/organization"
        params = {"server": server}
        if name:
            params["name"] = name

        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except HTTPError as e:
            error_detail = response.json().get("detail", str(e))
            raise ValueError(f"Error listing organizations: {error_detail}")
