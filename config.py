import os

flask_app_config = {
    "debug": os.environ.get("FLUSK_DEBUG_OPTION", True),
    "host": os.environ.get("FLASK_HOST", None),
    "port": os.environ.get("FLASK_PORT", 5000),
}



print(flask_app_config)
