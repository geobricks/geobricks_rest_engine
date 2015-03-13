settings = {

    # To be used by Flask: DEVELOPMENT ONLY
    "debug": True,

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

            # The name of the Blueprint
            # The name of the Blueprint variable in the "geobricks_distribution.rest.distribution_rest" module
            "blueprint_name": "app",

            # The prefix to be used for the Blueprint
            "url_prefix": "/common"
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