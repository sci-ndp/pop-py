from .get_method import APIClientGet
from .post_method import APIClientPost
from .delete_method import APIClientDelete
from .register_kafka_method import APIClientKafkaRegister


class APIClient(
    APIClientGet, APIClientPost, APIClientDelete, APIClientKafkaRegister
):
    """Unified API Client with GET, POST, and DELETE methods."""

    pass
