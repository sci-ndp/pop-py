from .client_base import APIClientBase
from requests.exceptions import HTTPError


class APIClientResourceDelete(APIClientBase):
    """Extension of APIClientBase with resource deletion methods."""

    def delete_resource_by_id(self, resource_id, server="local"):
        """
        Delete a resource by its ID by making a DELETE request.

        :param resource_id: ID of the resource to delete.
        :param server: Specify 'local' or 'pre_ckan'. Defaults to 'local'.
        :return: Response JSON data indicating success.
        :raises ValueError: If the deletion fails.
        """
        url = f"{self.base_url}/resource"
        params = {"resource_id": resource_id, "server": server}

        try:
            response = self.session.delete(url, params=params)
            response.raise_for_status()
            return response.json()
        except HTTPError as e:
            error_detail = response.json().get("detail", str(e))
            if "Resource not found" in error_detail:
                raise ValueError("Error deleting resource: Not found")
            else:
                raise ValueError(f"Error deleting resource: {error_detail}")

    def delete_resource_by_name(self, resource_name, server="local"):
        """
        Delete a resource by its name by making a DELETE request.
        """
        url = f"{self.base_url}/resource/{resource_name}"
        params = {"server": server}

        try:
            response = self.session.delete(url, params=params)
            response.raise_for_status()
            return response.json()
        except HTTPError as e:
            error_detail = response.json().get("detail", str(e))
            if "Resource not found" in error_detail:
                raise ValueError("Error deleting resource: Not found")
            else:
                raise ValueError(f"Error deleting resource: {error_detail}")
