# -*- coding: utf-8 -*-
import subprocess
from flask import Flask, request
import settings

app = Flask(__name__)


@app.route('/', methods=['POST'])
def webhook():
    if request.get_json():
        branch = request.get_json().get('ref')

        if branch == 'refs/heads/master':
            subprocess.call(['./webhook.sh', settings.PROJECT_DIR, settings.VIRTUALENV, settings.GUNICORN_PID_FILE])
            return "Successfully deployed new version"


if __name__ == '__main__':
    app.run()