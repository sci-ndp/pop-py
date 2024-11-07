from .get_method import APIClientGet
from .delete_method import APIClientDelete
from .register_kafka_method import APIClientKafkaRegister
from .register_organization_method import APIClientOrganizationRegister
from .register_s3_method import APIClientS3Register
from .register_url_method import APIClientURLRegister
from .list_organization_method import APIClientOrganizationList
from .search_method import APIClientSearch


class APIClient(
    APIClientGet,
    APIClientDelete,
    APIClientKafkaRegister,
    APIClientOrganizationRegister,
    APIClientS3Register,
    APIClientURLRegister,
    APIClientOrganizationList,
    APIClientSearch,
):
    """Unified API Client with GET, POST, and DELETE methods."""

    pass
