# -*- coding: utf-8 -*-
from werkzeug.contrib.fixers import ProxyFix
from webhook import app

__author__ = 'mkr'

app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.run()