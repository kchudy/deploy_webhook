# -*- coding: utf-8 -*-
import subprocess
from flask import Flask
import settings

app = Flask(__name__)


@app.route('/')
def webhook():
    subprocess.call(['./webhook', settings.PROJECT_DIR, settings.VIRTUALENV, settings.GUNICORN_PID_FILE])
    return "Successfully deployed new version"

if __name__ == '__main__':
    app.run()
