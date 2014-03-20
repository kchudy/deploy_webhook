#!/bin/bash

PROJECT_DIR=$1
VIRTUALENV=$2
GUNICORN_PID_FILE=$3
BRANCH=$4
SETTINGS_MODULE=$5

cd ${PROJECT_DIR}

git checkout ${BRANCH}
git pull origin ${BRANCH}

if [ -f ${GUNICORN_PID_FILE} ];
then
    kill `cat ${GUNICORN_PID_FILE}`
fi

source ${VIRTUALENV}/bin/activate
pip install -r requirements.txt

export ${SETTINGS_MODULE}
gunicorn -c gunicorn.py wsgi:myhoard