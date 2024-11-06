# pointofpresence/register_s3_method.py

from .client_base import APIClientBase
from requests.exceptions import HTTPError


class APIClientS3Register(APIClientBase):
    """Extension of APIClientBase with S3 resource registration method."""

    def register_s3_link(self, data):
        """
        Register a new S3 resource by making a POST request.

        :param data: Data for the S3 resource.
        :return: Response JSON data with the resource ID.
        :raises ValueError: If the registration fails.
        """
        url = f"{self.base_url}/s3"
        try:
            response = self.session.post(url, json=data)
            response.raise_for_status()
            return response.json()
        except HTTPError as e:
            error_detail = response.json().get("detail", str(e))
            if "Reserved key error" in error_detail:
                raise ValueError(
                    "Error creating S3 resource: Reserved key conflict."
                )
            elif "Invalid input" in error_detail:
                raise ValueError(
                    "Error creating S3 resource: Invalid input provided."
                )
            else:
                raise ValueError(f"Error creating S3 resource: {error_detail}")
