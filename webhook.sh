#!/bin/bash

PROJECT_DIR=$1
VIRTUALENV=$2
GUNICORN_PID_FILE=$3

cd $PROJECT_DIR

git pull origin master

if [ -f $GUNICORN_PID_FILE ];
then
    kill `cat $GUNICORN_PID_FILE`
fi

source $VIRTUALENV/bin/activate
pip install -r requirements.txt
gunicorn -c gunicorn.py wsgi:myhoard