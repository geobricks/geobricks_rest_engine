settings = {
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