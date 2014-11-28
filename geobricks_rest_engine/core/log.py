import logging
from geobricks_rest_engine.config.common_settings import settings

config = {
    # Logging configurations
    "logging": {
        "level": settings["settings"]["logging"]["level"],
        "format": "%(asctime)s | %(levelname)-8s | %(name)-20s | Line: %(lineno)-5d | %(message)s",
        "datefmt": "%d-%m-%Y | %H:%M:%s"
    }
}


level = config["logging"]["level"]
format = config["logging"]["format"]
datefmt = config["logging"]["datefmt"]
logging.basicConfig(level=level, format=format, datefmt=datefmt)


def logger(loggerName=None):
    logger = logging.getLogger(loggerName)
    logger.setLevel(level)
    return logger