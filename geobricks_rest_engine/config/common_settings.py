import logging
import os
import json

settings = {

    "settings": {


        # To be used by Flask: DEVELOPMENT ONLY
        "debug": True,

        # Flask host: DEVELOPMENT ONLY
        "host": "localhost",

        # Flask port: DEVELOPMENT ONLY
        "port": 5555,

        # Logging configurations
        "logging": {
            "level": logging.ERROR,
            "format": "%(asctime)s | %(levelname)-8s | %(name)-20s | Line: %(lineno)-5d | %(message)s",
            "datefmt": "%d-%m-%Y | %H:%M:%s"
        },

        # Email configurations
        "email": {
            "settings": "path_to_the_email.json",
            "user":  None,
            "password": None
        },

        # Folders
        "folders": {
            "config": "config/",
            "tmp": "tmp_path",
            "geoserver_datadir": "geoserver_data_folder",
            "distribution": "distribution_folder",
            "ftp": "ftp_folder"
        },

        "db": {
            # Spatial Database
            "spatial": {
                # default_db will search in the dbs["database"] as default option
                "dbname": "dbname",
                "host": "hostname",
                "port": "5432",
                "username": "user",
                "password": "pwd",
                "schema": "public"
            }
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
        }
    }
}


# Setting email adderess from configuration file
def set_email_settings():
    if os.path.isfile(settings["settings"]["email"]["settings"]):
        settings["settings"]["email"] = json.loads(open(settings["settings"]["email"]["settings"]).read())
set_email_settings()