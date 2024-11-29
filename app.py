import time
import os
from flask import Flask
from events import socketio
import config

import module

app = Flask(__name__)

print("ECCOMI QUA")
print("host:",os.environ["FLASK_RUN_HOST"])
print("env:",os.environ)

@app.route('/')
def hello():
    print("ho ricevuto la chiamata")
    num = module.print_random()
    count = 1
    print("adesso ritorno")
    return f'Hello World! I have been seen {count} times.\n Random generated number {num}\n NO WAY FUNZIONA'


if __name__ == '__main__':
    socketio.init_app(app)
    socketio.run(app,**config.flask_app_config)