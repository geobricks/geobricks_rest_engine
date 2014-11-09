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
            "description": "MODIS",

            # The path to the Python file containing the Blueprint
            "path_to_the_blueprint": "geobricks_modis.rest.modis_rest",

            # The name of the Blueprint
            "blueprint_name": "modis",

            # The prefix to be used for the Blueprint
            "url_prefix": "/browse/modis"

        }

    ]

}