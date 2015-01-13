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
            "tmp": "/tmp/",
            "geoserver_datadir": "geoserver_data_dir/",
            "distribution": "distribution/",
            "storage": "storage/",
            # this is used by the filesystem to get the (published) layers in the file system
            "workspace_layer_separator": ":"
        },

        # Database
        "db": {
            # Spatial Database
            "spatial": {
                # default_db will search in the dbs["database"] as default option
                "dbname": "db",
                "host": "localhost",
                "port": "5432",
                "username": "user",
                "password": "pwd",
                "schema": "public",
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
            "url_create_metadata": "//localhost/d3s_dev/msd/resources/metadata",
            "url_get_metadata_uid": "//localhost/d3s_dev/msd/resources/metadata/uid/<uid>",

            # delete metadata
            "url_delete_metadata": "//localhost/d3s_dev/msd/resources/metadata/uid/<uid>",

            # get metadata
            "url_get_metadata": "//localhost/d3s_dev/msd/resources/find",
            "url_get_metadata_full": "//localhost/d3s_dev/msd/resources/metadata/uid/<uid>?full=true&dsd=true",

            # coding system
            "url_create_coding_system": "//localhost/d3s_dev/msd/resources",
            "url_data_coding_system": "//localhost/d3s_dev/msd/resources/data/uid/<uid>",

            # DSD
            "url_overwrite_dsd_rid": "//localhost/d3s_dev/msd/resources/dsd"
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