# -*- coding: utf-8 -*-
import importlib
import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def webhook():
    if request.get_json():
        ref = request.get_json().get('ref')
        branch = ref[ref.rfind("/")+1:]

        try:
            settings = importlib.import_module("settings.%s" % branch)
        except ImportError, e:
            return 'Settings import failed. Details: %s' % e.message
        except AttributeError, e:
            return 'Settings import failed. Details: %s' % e.message

        subprocess.call(['./webhook.sh', settings.PROJECT_DIR, settings.VIRTUALENV, settings.GUNICORN_PID_FILE, branch])
        return 'Successfully deployed new version'
    return ''

if __name__ == '__main__':
    app.run()