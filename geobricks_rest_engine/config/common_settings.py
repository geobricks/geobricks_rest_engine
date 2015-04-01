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
            "user": "user",
            "password": "password"
        },

        # Folders
        "folders": {
            "tmp": "/home/vortex/Desktop/LAYERS/geobricks/tmp/",
            "geoserver_datadir": "/home/vortex/programs/SERVERS/tomcat_geoservers/data/",
            "distribution": "/home/vortex/Desktop/LAYERS/geobricks/distribution",
            "distribution_sld": "/home/vortex/repos/FENIX-MAPS/geobricks/geobricks_sld/distribution_sld/",
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
                "username": "user",
                "password": "pwd",
                "schema": "schema"
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