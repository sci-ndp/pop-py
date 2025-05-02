# National Data Platform (NDP) Tutorial Documentation

This documentation explains the usage of the NDP End Point (EP) library through the tutorial notebook `pop_0.5.2_with_NDP.ipynb`.

## Overview

The tutorial notebook demonstrates how to:
- Connect to the National Data Platform (NDP)
- Manage organizations and resources
- Send data to the NDP pre-CKAN staging area
- Search and discover datasets

## Using the Notebook

### Prerequisites
1. Install the required library:
```bash
pip install pointofpresence
```

2. Obtain an NDP token from: https://token.ndp.utah.edu/

### Starting the Notebook
1. Navigate to the `docs` directory
2. Launch Jupyter: `jupyter notebook`
3. Open `pop_0.5.2_with_NDP.ipynb`

### Configuration
```python
# Set up API connection
api_base_url = "http://155.101.6.191:8003/"
api_token = "your_ndp_token"

# Initialize client
from pointofpresence import APIClient
client = APIClient(base_url=api_base_url, token=api_token)
```

## Key Concepts

### Organizations
Organizations in NDP serve as logical groupings for resources and datasets:
- Act as containers for related datasets
- Help manage access control and permissions
- Enable better organization of data resources
- Allow team collaboration on datasets

### Resource Types
NDP supports three types of resources:

1. **Kafka Topics**
   - For streaming data
   - Real-time data processing
   - Continuous data flows

2. **S3 Links**
   - For object storage
   - Large dataset management
   - Static file storage

3. **URL Resources**
   - External data sources
   - Web-accessible datasets
   - Supports multiple file types (CSV, JSON, TXT, NetCDF)

## Sending Data to NDP Pre-CKAN

### Process Overview
1. **Registration**: Register your organization and resources
2. **Pre-CKAN**: Send data to the staging area using `server="pre_ckan"`
3. **Review**: Data is reviewed for quality and compliance
4. **Approval**: Approved data moves to the public catalog

### Example Workflow
```python
# Register organization in pre-CKAN
org_data = {
    "name": "my_organization",
    "title": "My Organization",
    "description": "Organization description"
}
client.register_organization(org_data, server="pre_ckan")

# Register resource in pre-CKAN
resource_data = {
    "resource_name": "my_dataset",
    "resource_title": "My Dataset",
    "owner_org": "my_organization",
    # ... other required fields
}
client.register_url(resource_data, server="pre_ckan")
```

## Detailed API Endpoints

### Organization Management

#### 1. Register Organization
```python
org_data = {
    "name": "my_organization",
    "title": "My Organization",
    "description": "Organization description"
}
client.register_organization(org_data, server="pre_ckan")
```

#### 2. List Organizations
```python
# List all organizations
orgs = client.list_organizations(server="local")

# Filter organizations
filtered_orgs = client.list_organizations(name="example", server="local")
```

#### 3. Delete Organization
```python
client.delete_organization("organization_name", server="local")
```

### Resource Management

#### 1. Kafka Topics
```python
# Register Kafka Topic
kafka_data = {
    "dataset_name": "my_kafka_dataset",
    "dataset_title": "My Kafka Stream",
    "owner_org": "my_organization",
    "kafka_topic": "my_topic",
    "kafka_host": "kafka_host",
    "kafka_port": "9092",
    "dataset_description": "Real-time data stream",
    "extras": {"source": "sensor_network"}
}
client.register_kafka_topic(kafka_data)

# Get Kafka Details
kafka_info = client.get_kafka_details()
```

#### 2. S3 Resources
```python
# Register S3 Resource
s3_data = {
    "resource_name": "my_s3_resource",
    "resource_title": "S3 Dataset",
    "owner_org": "my_organization",
    "resource_s3": "s3://bucket-name/path",
    "notes": "Large dataset storage"
}
client.register_s3_link(s3_data)
```

#### 3. URL Resources
```python
# Register URL Resource
url_data = {
    "resource_name": "my_url_resource",
    "resource_title": "External Dataset",
    "owner_org": "my_organization",
    "resource_url": "http://example.com/data.csv",
    "file_type": "CSV",
    "processing": {
        "delimiter": ",",
        "header_line": 1,
        "start_line": 2
    }
}
client.register_url(url_data)
```

### Search Operations

#### 1. Global Search
```python
# Search across all fields
results = client.search_datasets(
    terms=["temperature", "humidity"],
    server="global"
)
```

#### 2. Field-Specific Search
```python
# Search in specific fields
results = client.search_datasets(
    terms=["sensor", "temperature"],
    keys=["extras.device_type", "description"],
    server="global"
)
```

### Resource Deletion

```python
# Delete by ID
client.delete_resource_by_id("resource_id")

# Delete by Name
client.delete_resource_by_name("resource_name")
```

## Common Use Cases

### 1. Setting up a Data Stream
```python
# 1. Create organization
org_data = {
    "name": "weather_org",
    "title": "Weather Monitoring",
    "description": "Weather sensor network data"
}
client.register_organization(org_data, server="pre_ckan")

# 2. Register Kafka topic
kafka_data = {
    "dataset_name": "weather_stream",
    "dataset_title": "Real-time Weather Data",
    "owner_org": "weather_org",
    "kafka_topic": "weather_sensors",
    "kafka_host": "kafka_host",
    "kafka_port": "9092"
}
client.register_kafka_topic(kafka_data)
```

### 2. Batch Data Upload
```python
# 1. Prepare data resource
resource_data = {
    "resource_name": "weather_2023",
    "resource_title": "Weather Data 2023",
    "owner_org": "weather_org",
    "resource_url": "http://example.com/weather2023.csv",
    "file_type": "CSV",
    "processing": {
        "delimiter": ",",
        "header_line": 1
    }
}

# 2. Register in pre-CKAN
client.register_url(resource_data, server="pre_ckan")
```

## Benefits

### 1. Data Organization
- Hierarchical structure through organizations
- Logical grouping of related datasets
- Clear ownership and responsibility

### 2. Data Discovery
- Powerful search capabilities
- Metadata-based discovery
- Field-specific searching

### 3. Data Integration
- Multiple resource types support
- Standardized data access
- Federated data catalog

### 4. Data Governance
- Pre-CKAN staging area
- Quality control through review process
- Access control through organizations

## Best Practices

1. **Organization Management**
   - Use clear, descriptive names
   - Provide detailed descriptions
   - Maintain consistent naming conventions

2. **Resource Registration**
   - Include comprehensive metadata
   - Use appropriate resource types
   - Follow data quality guidelines

3. **Pre-CKAN Usage**
   - Test data locally first
   - Validate data structure
   - Include all required metadata

4. **Search Optimization**
   - Use specific search keys
   - Combine global and field-specific searches
   - Utilize metadata fields effectively

## Additional Resources

- NDP Token Registration: https://token.ndp.utah.edu/
- API Documentation: [Link to API docs]
- Support Contact: [Contact information]

## Error Handling

The notebook includes comprehensive error handling for common scenarios:
- Authentication failures
- Resource conflicts
- Invalid data formats
- Missing required fields

## Conclusion

The NDP EP library provides a robust interface for managing and sharing data through the National Data Platform. By following this tutorial and documentation, users can effectively utilize the platform's features for data management and collaboration.

## NDP Metadata Guidelines

### Required Metadata Fields

When registering resources in pre-CKAN, ensure the following required fields are provided:

#### Dataset Level (Required)
```python
dataset_metadata = {
    "title": "Dataset Title",                    # Required: dct:title
    "notes": "Dataset Description",              # Required: dct:description
    "tags": ["tag1", "tag2"],                   # Required: dcat:keyword
    "extras": {
        "creation_method": "method_name",        # Required
        "issued": "2024-02-07",                 # Required: dct:issued
        "modified": "2024-02-07",               # Required: dct:modified
        "type_of_entity": "Data",               # Required: One of [Data, Model, Service, DockerImage]
        "purpose": "Dataset purpose",            # Required: dcat:us:purpose
        "data_type": "dataset_type",            # Required: dct:type
        
        # Publisher Information (Required)
        "publisher_name": "Publisher Name",      # Required: foaf:name
        "publisher_email": "pub@example.com",    # Required: foaf:mbox
        
        # Creator Information (Required)
        "creator_name": "Creator Name",          # Required: foaf:name
        "creator_email": "creator@example.com",  # Required: foaf:mbox
        
        # Point of Contact Information (Required)
        "contact_name": "Contact Name",          # Required: foaf:name
        "contact_email": "contact@example.com"   # Required: foaf:mbox
    }
}
```

### Resource Level Metadata

#### URL Resource (Required Fields)
```python
url_resource = {
    "resource_name": "Resource Title",           # Required: dct:title
    "resource_description": "Description",       # Required: dct:description
    "resource_url": "http://example.com/data",   # Required: Either accessURL or downloadURL
    "mimetype": "text/csv",                     # Required: dcat:mediaType
    "format": "CSV",                            # Required: dct:format
    "status": "active"                          # Required: adms:status
}
```

### Optional but Recommended Fields

#### Dataset Level
```python
optional_metadata = {
    "extras": {
        "theme": ["theme1", "theme2"],          # dcat:theme
        "doi": "10.xxxx/xxxxx",                 # dct:identifier
        "dataset_version": "1.0.0",             # owl:versionInfo
        "version_notes": "Version details",      # adms:versionNotes
        "language": "en",                        # dct:language
        "dataset_page_url": "http://...",       # dcat:landingPage
        "update_freq": "daily",                 # dct:accrualPeriodicity
        "access_rights": "public",              # dct:accessRights
        "documentation": "http://docs...",      # foaf:page
        "data_provenance": "source details",    # dct:provenance
        "usage_info": "usage guidelines",       # skos:scopeNote
        
        # Temporal Coverage
        "temporal_start": "2024-01-01",         # dct:temporal
        "temporal_end": "2024-12-31",           # dct:temporal
        "temporal_resolution": "1 day",         # dcat:temporalResolution
        
        # Spatial Coverage
        "spatial_uri": "geojson or wkt string", # dct:spatial
        "bbox": "bounding box data",            # dcat:us:geographicBoundingBox
        "spatial_resolution_in_meters": 30,      # dcat:spatialResolutionInMeters
        
        # Additional Metadata
        "data_dictionary": [                    # dcat:us:describedBy
            {
                "column": "column_name",
                "description": "description",
                "type": "data_type"
            }
        ]
    }
}
```

### Best Practices for Metadata

1. **Completeness**
   - Provide all required fields
   - Include optional fields when available
   - Use standardized formats for dates (ISO 8601)

2. **Quality**
   - Use clear, descriptive titles
   - Write comprehensive descriptions
   - Include detailed contact information
   - Provide accurate temporal and spatial coverage

3. **Consistency**
   - Use consistent naming conventions
   - Maintain consistent date formats
   - Follow standardized vocabularies for themes and keywords

4. **Data Dictionary**
   - Include column definitions
   - Specify data types
   - Document units of measurement
   - Explain any codes or abbreviations

### Example Usage

```python
# Register a dataset with metadata
dataset_data = {
    "title": "Weather Observations 2024",
    "notes": "Hourly weather observations from multiple stations",
    "tags": ["weather", "observations", "hourly"],
    "extras": {
        "creation_method": "automated_collection",
        "issued": "2024-02-07",
        "modified": "2024-02-07",
        "type_of_entity": "Data",
        "purpose": "Climate monitoring and analysis",
        "data_type": "observational",
        "publisher_name": "Weather Service",
        "publisher_email": "weather@service.com",
        "temporal_start": "2024-01-01",
        "temporal_end": "2024-12-31",
        "temporal_resolution": "1 hour",
        "spatial_resolution_in_meters": 1000
    }
}

# Register the dataset in pre-CKAN
response = client.register_url(dataset_data, server="pre_ckan")
```
