# pointofpresence/register_kafka_method.py

from .client_base import APIClientBase
from requests.exceptions import HTTPError


class APIClientKafkaRegister(APIClientBase):
    """Extension of APIClientBase with Kafka topic registration method."""

    def register_kafka_topic(self, data):
        """
        Register a new Kafka topic by making a POST request.

        :param data: Data for the Kafka topic.
        :return: Response JSON data with the topic ID.
        :raises ValueError: If the registration fails.
        """
        url = f"{self.base_url}/kafka"
        try:
            response = self.session.post(url, json=data)
            response.raise_for_status()
            return response.json()
        except HTTPError as e:
            raise ValueError(f"Error creating Kafka dataset: {str(e)}")
