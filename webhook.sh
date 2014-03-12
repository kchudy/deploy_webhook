#!/bin/bash

PROJECT_DIR=$1
VIRTUALENV=$2
GUNICORN_PID_FILE=$3

cd PROJECT_DIR

git pull origin master

if [ -f $GUNICORN_PID_FILE ];
then
    kill `cat myhoard.pid`

source $VIRTUALENV/bin/activate

gunicorn -c gunicorn.py wsgi:myhoard
