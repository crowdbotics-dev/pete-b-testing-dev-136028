#!/bin/bash

python manage.py migrate --noinput

waitress-serve --port=$PORT pete_b_testing_dev_136028.wsgi:application
