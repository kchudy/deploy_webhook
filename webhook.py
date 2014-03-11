# -*- coding: utf-8 -*-
from fabric.context_managers import lcd
from fabric.operations import local, os
from flask import Flask
import settings

app = Flask(__name__)


@app.route('/')
def webhook():
    with lcd(settings.PROJECT_DIR):
        local('git pull origin master')
        current_hash = local('git rev-parse --short HEAD')

        if os.path.isfile(settings.GUNICORN_PID_FILE):
            with open(settings.GUNICORN_PID_FILE) as pidfile:
                gunicorn_pid = pidfile.read()
                local('kill %s' % gunicorn_pid)

        local('gunicorn -c gunicorn.py wsgi:myhoard')

    return "Successfully deployed version %s" % current_hash


if __name__ == '__main__':
    app.run()
