import logging
import os
import json

settings = {

    "settings": {

        # base url used by NGINX
        "base_url": "", #(i.e. "demo/geo/ghg/"),

        # Logging configurations
        "logging": {
            "level": logging.INFO,
            "format": "%(asctime)s | %(levelname)-8s | %(name)-20s | Line: %(lineno)-5d | %(message)s",
            "datefmt": "%d-%m-%Y | %H:%M:%s"
        },

        # Email configurations (for now uses gmail as default client)
        "email": {
            "user":  "user",
            "password": "password"
        },

        # Folders
        "folders": {
            "tmp": "/home/vortex/Desktop/LAYERS/geobricks/tmp/",
            "geoserver_datadir": "/home/vortex/programs/SERVERS/tomcat_geoservers/data/",
            "distribution": "/home/vortex/Desktop/LAYERS/geobricks/distribution",
            "storage": "/home/vortex/Desktop/LAYERS/geobricks/storage/",
            # this is used by the filesystem to get the (published) layers in the file system
            "workspace_layer_separator": ":"
        },

        # Database
        "db": {
            # Spatial Database
            "spatial": {
                # default_db will search in the dbs["database"] as default option
                "dbname": "fenix",
                "host": "localhost",
                "port": "5432",
                "username": "fenix",
                "password": "Qwaszx",
                "schema": "spatial",

                # TODO: move to the metadata DB? layers to be used as default ones
                "tables": {
                    # bbox
                    "country": {

                        # table mapped in the database
                        "table": "gaul0_2015_4326",

                        # alias to use in the columns
                        "column": {
                            "code": "adm0_name",
                            "label": "adm0_name",
                            "adm0_code": "adm0_code",
                            "iso2": "iso2",
                            "iso3": "iso3",

                            # geometry column
                            "geom": "geom"
                        },

                        # srid used TODO: better projection?
                        "srid": "4326",
                        },
                    "gaul0": {
                        "table": "gaul0_2015_4326",
                        "column_grom": "geom",
                        "srid": "4326"
                    },
                    "gaul1": {
                        "table": "gaul1_2015_4326",
                        "column_grom": "geom",
                        "srid": "4326"
                    }
                }
            },
            },

        # Storage remove Configuration
        "storage": {
            "url": "localhost",
            "user": "user",
            "password": "password"
        },

        # Metadata settings
        "metadata": {
            "url_create_metadata": "http://fenix.fao.org/d3s_dev/msd/resources/metadata",
            "url_get_metadata_uid": "http://fenix.fao.org/d3s_dev/msd/resources/metadata/uid/<uid>",

            # delete metadata
            "url_delete_metadata": "http://fenix.fao.org/d3s_dev/msd/resources/metadata/uid/<uid>",

            # get metadata
            "url_get_metadata": "http://fenix.fao.org/d3s_dev/msd/resources/find",
            "url_get_metadata_full": "http://fenix.fao.org/d3s_dev/msd/resources/metadata/uid/<uid>?full=true&dsd=true",

            # coding system
            "url_create_coding_system": "http://fenix.fao.org/d3s_dev/msd/resources",
            "url_data_coding_system": "http://fenix.fao.org/d3s_dev/msd/resources/data/uid/<uid>",

            # DSD
            "url_overwrite_dsd_rid": "http://fenix.fao.org/d3s_dev/msd/resources/dsd"
        },

        # Geoserver settings
        "geoserver": {
            "geoserver_master": "http://localhost:9090/geoserver/rest",
            "geoserver_slaves": [],
            "username": "admin",
            "password": "geoserver",
            }
    }
}


# Setting email adderess from configuration file
def set_email_settings():
    if "email" in settings["settings"]:
        if "settings" in settings["settings"]["email"] and os.path.isfile(settings["settings"]["email"]["settings"]):
            settings["settings"]["email"] = json.loads(open(settings["settings"]["email"]["settings"]).read())
set_email_settings()