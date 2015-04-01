settings = {

    "settings": {

        # To be used by Flask: DEVELOPMENT ONLY
        "debug": False,

        # Flask host: DEVELOPMENT ONLY
        "host": "localhost",

        # Flask port: DEVELOPMENT ONLY
        "port": 5555,

        # List of modules to be imported at the start-up.
        "modules": [
            {
                # Description, not used by the code.
                "description": "geobricks_common",

                # The path to the Python file containing the configuration
                "path_to_the_config": "geobricks_common.config.config",

                # The path to the Python file containing the Blueprint
                "path_to_the_blueprint": "geobricks_common.rest.common_rest",

                # The path to the Python file containing the configuration
                "path_to_the_config": "geobricks_common.config.config",

                # The name of the Blueprint
                "blueprint_name": "app",

                # The prefix to be used for the Blueprint
                "url_prefix": "/common"
            },
            {
                # Description, not used by the code.
                "description": "GIS Raster",
                # The path to the Python file containing the configuration
                "path_to_the_config": "geobricks_gis_raster.config.config",
            },
            {
                # Description, not used by the code.
                "description": "GIS Vector",
                # The path to the Python file containing the configuration
                "path_to_the_config": "geobricks_gis_vector.config.config",
            },
            {
                # Description, not used by the code.
                "description": "Geocoding",

                # The path to the Python file containing the Blueprint
                "path_to_the_blueprint": "geobricks_geocoding.rest.geocoding_rest",

                # The path to the Python file containing the configuration
                "path_to_the_config": "geobricks_geocoding.config.config",

                # The name of the Blueprint
                # The name of the Blueprint variable in the "geobricks_distribution.rest.distribution_rest" module
                "blueprint_name": "app",

                # The prefix to be used for the Blueprint
                "url_prefix": "/geocoding"
            },
            {
                # Description, not used by the code.
                "description": "Map Classify",

                # The path to the Python file containing the Blueprint
                "path_to_the_blueprint": "geobricks_mapclassify.rest.mapclassify_rest",

                # The path to the Python file containing the configuration
                "path_to_the_config": "geobricks_mapclassify.config.config",

                # The name of the Blueprint
                # The name of the Blueprint variable in the "geobricks_distribution.rest.distribution_rest" module
                "blueprint_name": "app",

                # The prefix to be used for the Blueprint
                "url_prefix": "/mapclassify"
            },
            {
                # Description, not used by the code.
                "description": "SpatialQuery",

                # The path to the Python file containing the Blueprint
                "path_to_the_blueprint": "geobricks_spatial_query.rest.spatial_query_rest",

                # The path to the Python file containing the configuration
                "path_to_the_config": "geobricks_spatial_query.config.config",

                # The name of the Blueprint
                "blueprint_name": "app",

                # The prefix to be used for the Blueprint
                "url_prefix": "/spatialquery"
            },
            {
                # Description, not used by the code.
                "description": "Metadata Manager",

                # The path to the Python file containing the Blueprint
                "path_to_the_blueprint": "geobricks_metadata_manager.rest.metadata_manager_rest",

                # The path to the Python file containing the configuration
                "path_to_the_config": "geobricks_metadata_manager.config.config",

                # The name of the Blueprint
                "blueprint_name": "app",

                # The prefix to be used for the Blueprint
                "url_prefix": "/metadata"
            },
            {
                # Description, not used by the code.
                "description": "Distribution",

                # The path to the Python file containing the Blueprint
                "path_to_the_blueprint": "geobricks_distribution.rest.distribution_rest",

                # The path to the Python file containing the configuration
                "path_to_the_config": "geobricks_distribution.config.config",

                # The name of the Blueprint
                "blueprint_name": "app",

                # The prefix to be used for the Blueprint
                "url_prefix": "/distribution"
            },
            {
                # Description, not used by the code.
                "description": "Geostatistics",

                # The path to the Python file containing the Blueprint
                "path_to_the_blueprint": "geobricks_geostatistics.rest.geostatistics_rest",

                # The path to the Python file containing the configuration
                "path_to_the_config": "geobricks_geostatistics.config.config",

                # The name of the Blueprint
                "blueprint_name": "app",

                # The prefix to be used for the Blueprint
                "url_prefix": "/geostatistics"
            },
            {
                # Description, not used by the code.
                "description": "DBMS",

                # The path to the Python file containing the Blueprint
                "path_to_the_blueprint": "geobricks_dbms.rest.dbms_rest",

                # The path to the Python file containing the configuration
                "path_to_the_config": "geobricks_dbms.config.dbms_config",

                # The name of the Blueprint
                "blueprint_name": "dbms",

                # The prefix to be used for the Blueprint
                "url_prefix": "/dbms"
            },
            {
                # Description, not used by the code.
                "description": "geobricks_processing",
                # The path to the Python file containing the configuration
                "path_to_the_config": "geobricks_processing.config.config",

                # The path to the Python file containing the Blueprint
                "path_to_the_blueprint": "geobricks_processing.rest.processing_rest",

                # The name of the Blueprint
                # The name of the Blueprint variable in the "geobricks_distribution.rest.distribution_rest" module
                "blueprint_name": "app",

                # The prefix to be used for the Blueprint
                "url_prefix": "/processing"
            },
            {

                # Description, not used by the code.
                "description": "MODIS",

                # The path to the Python file containing the Blueprint
                "path_to_the_blueprint": "geobricks_modis.rest.modis_rest",

                # The path to the Python file containing the configuration
                "path_to_the_config": "geobricks_modis.config.modis_config",

                # The name of the Blueprint
                "blueprint_name": "modis",

                # The prefix to be used for the Blueprint
                "url_prefix": "/browse/modis"

            },
            {
                # Description, not used by the code.
                "description": "DOWNLOAD",

                # The path to the Python file containing the Blueprint
                "path_to_the_blueprint": "geobricks_downloader.rest.downloader_rest",

                # The path to the Python file containing the configuration
                "path_to_the_config": "geobricks_downloader.config.downloader_config",

                # The name of the Blueprint
                "blueprint_name": "downloader",

                # The prefix to be used for the Blueprint
                "url_prefix": "/download"
            }
        ]
    }
}