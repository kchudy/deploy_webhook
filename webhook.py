# -*- coding: utf-8 -*-
import importlib
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['POST'])
def webhook():
    if request.get_json():
        ref = request.get_json().get('ref')
        branch = ref[ref.rfind("/") + 1:]

        try:
            settings = importlib.import_module("settings.%s" % branch)
        except ImportError, e:
            return 'Settings import failed. Details: %s' % e.message

        exit_code = subprocess.call(['./webhook.sh', settings.PROJECT_DIR, settings.VIRTUALENV, settings.GUNICORN_PID_FILE, branch, settings.SETTINGS_MODULE, settings.LOGS_DIR])

        response = {
            'exit_code': exit_code,
            'branch': branch
        }
        return jsonify(**response)
    return ''


if __name__ == '__main__':
    app.run()