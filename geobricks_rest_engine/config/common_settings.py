import logging
import os
import json

settings = {

    "settings": {

        # base url used by nginx
        "base_url": "", #(i.e. "demo/geo/ghg/"),

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
            "tmp": "tmp_path",
            "geoserver_datadir": "geoserver_data_folder",
            "distribution": "distribution_folder",
            "ftp": "ftp_folder",
            # this is used by the filesystem to get the (published) layers in the file system
            "workspace_layer_separator": "@"
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

        # metdata settings
        "metadata": {
            "url_create_metadata": "http://exldvsdmxreg1.ext.fao.org:7788/v2/msd/resources/metadata",
            "url_get_metadata_uid": "http://exldvsdmxreg1.ext.fao.org:7788/v2/msd/resources/metadata/uid/<uid>?full=true&dsd=true",
            # get metadata
            "url_get_metadata": "http://exldvsdmxreg1.ext.fao.org:7788/v2/msd/resources/metadata/uid/<uid>",
            "url_get_full_metadata": "http://exldvsdmxreg1.ext.fao.org:7788/v2/msd/resources/metadata/uid/<uid>?full=true&dsd=true",
            # coding system
            "url_create_coding_system": "http://exldvsdmxreg1.ext.fao.org:7788/v2/msd/resources",
            "url_data_coding_system": "http://exldvsdmxreg1.ext.fao.org:7788/v2/msd/resources/data/uid/<uid>",
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