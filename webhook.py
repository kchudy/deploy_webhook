# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)


@app.route('/')
def webhook():
    return 'MyHoard WebHook works fine dude!'


if __name__ == '__main__':
    app.run()
