#!/bin/bash

cd /var/www/tasks.zz50.co.uk
export FLASK_ENV=development

flask run --host=0.0.0.0 --port=80
