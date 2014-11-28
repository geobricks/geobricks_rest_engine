import logging

settings = {

    "settings": {

        # Logging configurations
        "logging": {
            "level": logging.INFO,
            "format": "%(asctime)s | %(levelname)-8s | %(name)-20s | Line: %(lineno)-5d | %(message)s",
            "datefmt": "%d-%m-%Y | %H:%M:%s"
        },


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