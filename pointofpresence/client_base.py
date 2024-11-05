import requests


class APIClientBase:
    """Base class for the API client."""

    def __init__(
        self, base_url: str, username: str = None, password: str = None
    ):
        """
        Initialize the API client.

        :param base_url: Base URL of the API.
        :param username: Username for authentication.
        :param password: Password for authentication.
        """
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.token = None

        if username and password:
            self.get_token(username, password)

    def get_token(self, username: str, password: str):
        """
        Obtain authentication token.

        :param username: Username for authentication.
        :param password: Password for authentication.
        """
        url = f"{self.base_url}/token"
        response = self.session.post(
            url, data={"username": username, "password": password}
        )
        response.raise_for_status()
        self.token = response.json().get("access_token")
        if not self.token:
            raise ValueError(
                "Authentication failed: No access token received."
            )
        self.session.headers.update({"Authorization": f"Bearer {self.token}"})
