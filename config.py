import os

flask_app_config = {
    "debug": os.environ.get("FLUSK_DEBUG_OPTION", True),
    "host": os.environ.get("FLASK_HOST", None),
    "port": os.environ.get("FLASK_PORT", 5000),
    #"ssl_context": os.environ.get("SSL_CONTEX","adhoc"),
    #"allow_unsafe_werkzeug": os.environ.get("UNSAFE_WERKZEUG",True),
}



print(flask_app_config)
