#!/bin/bash

cd /var/www/tasks.zz50.co.uk
export FLASK_ENV=development

if [[ $1 = 'dev' ]]; then
    export FLASK_APP=tasks.py
    flask run --host=0.0.0.0 --port=5000
else
    flask run --host=0.0.0.0 --port=80
fi
