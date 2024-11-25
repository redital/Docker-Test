import time

from flask import Flask

import module

app = Flask(__name__)

print("ECCOMI QUA")

@app.route('/')
def hello():
    print("ho ricevuto la chiamata")
    num = module.print_random()
    count = 1
    print("adesso ritorno")
    return f'Hello World! I have been seen {count} times.\n Random generated number {num}\n NO WAY FUNZIONA'