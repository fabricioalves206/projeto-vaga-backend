#!/bin/bash

set -e

python manage.py makemigrations
python manage.py migrate

python manage.py loaddata user_department_api/fixtures/inital_data.json

exec "$@"