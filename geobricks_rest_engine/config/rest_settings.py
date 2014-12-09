settings = {

    # To be used by Flask: DEVELOPMENT ONLY
    "debug": True,

    # Flask host: DEVELOPMENT ONLY
    "host": "168.202.28.214",

    # Flask port: DEVELOPMENT ONLY
    "port": 7777,

    # List of modules to be imported at the start-up.
    "modules": [
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
            "description": "Metadata Manager",

            # The path to the Python file containing the Blueprint
            "path_to_the_blueprint": "geobricks_metadata_manager.rest.metadata_manager_rest",

            # The path to the Python file containing the configuration
            "path_to_the_config": "geobricks_metadata_manager.config.config",

            # The name of the Blueprint
            # The name of the Blueprint variable in the "geobricks_distribution.rest.distribution_rest" module
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
            # The name of the Blueprint variable in the "geobricks_distribution.rest.distribution_rest" module
            "blueprint_name": "app",

            # The prefix to be used for the Blueprint
            "url_prefix": "/distribution"
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