import logging
import os
import json

settings = {

    "settings": {

        # Logging configurations
        "logging": {
            "level": logging.ERROR,
            "format": "%(asctime)s | %(levelname)-8s | %(name)-20s | Line: %(lineno)-5d | %(message)s",
            "datefmt": "%d-%m-%Y | %H:%M:%s"
        },

        # Email configurations
        "email": {
            "settings": "/home/vortex/Desktop/LAYERS/email.json",
            "user":  None,
            "password": None
        },

        # Folders
        "folders": {
            "config": "config/",
            "tmp": "/home/vortex/Desktop/LAYERS/tmp",
            "data_providers": "data_providers/",
            "metadata": "metadata/",
            "stats": "stats/",
            "geoserver": "geoserver/",
            "metadata_templates": "metadata/templates/",
            # used on runtime statistics (for Published layers this is the Geoservers Cluster "datadir")
            "geoserver_datadir": "/home/vortex/programs/SERVERS/tomcat_geoservers/data/",
            #"geoserver_datadir": "/home/vortex/Desktop/LAYERS/GEOSERVER_TEST",

            "distribution": "/home/vortex/Desktop/LAYERS/DISTRIBUTION/"
        },

        # Downloads
        "target_root": "/home/kalimaha/Desktop/GIS/MODIS",
        "target": {
            "folders": [
                {
                    "folder_name": "{{product}}",
                    "folders": [
                        {
                            "folder_name": "{{year}}",
                            "folders": [
                                {
                                    "folder_name": "{{day}}"
                                }
                            ]
                        }
                    ]
                }
            ],
            "bands": [
                {
                    "index": 1,
                    "label": "NDVI"
                },
                {
                    "index": 2,
                    "label": "EVI"
                }
            ],
            "subfolders": {
                "output": "OUTPUT"
            }
        },

        # FIXME: it depends on the product...
        "bands": [
            {
                "index": 1,
                "label": "NDVI"
            },
            {
                "index": 2,
                "label": "EVI"
            }
        ],

        "subfolders": {
            "output": "OUTPUT"
        },

        # To be used by Flask: DEVELOPMENT ONLY
        "debug": True,

        # Flask host: DEVELOPMENT ONLY
        "host": "localhost",

        # Flask port: DEVELOPMENT ONLY
        "port": 5555
    }
}


# Setting email adderess from configuration file
def set_email_settings():
    if os.path.isfile(settings["settings"]["email"]["settings"]):
        settings["settings"]["email"] = json.loads(open(settings["settings"]["email"]["settings"]).read())
set_email_settings()