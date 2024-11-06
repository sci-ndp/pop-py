from .get_method import APIClientGet
from .post_method import APIClientPost
from .delete_method import APIClientDelete
from .register_kafka_method import APIClientKafkaRegister
from .register_organization_method import APIClientOrganizationRegister
from .register_s3_method import APIClientS3Register
from .register_url_method import APIClientURLRegister


class APIClient(
    APIClientGet,
    APIClientPost,
    APIClientDelete,
    APIClientKafkaRegister,
    APIClientOrganizationRegister,
    APIClientS3Register,
    APIClientURLRegister,
):
    """Unified API Client with GET, POST, and DELETE methods."""

    pass
