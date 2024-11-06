from .get_method import APIClientGet
from .post_method import APIClientPost
from .delete_method import APIClientDelete
from .register_kafka_method import APIClientKafkaRegister
from .register_organization_method import APIClientOrganizationRegister


class APIClient(
    APIClientGet,
    APIClientPost,
    APIClientDelete,
    APIClientKafkaRegister,
    APIClientOrganizationRegister,
):
    """Unified API Client with GET, POST, and DELETE methods."""

    pass
