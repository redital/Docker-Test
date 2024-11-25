import time

from flask import Flask

import module

app = Flask(__name__)


@app.route('/')
def hello():
    num = module.print_random()
    count = 1
    print("questo me lo stampi?")
    return f'Hello World! I have been seen {count} times.\n Random generated number {num}\n NO WAY FUNZIONA'