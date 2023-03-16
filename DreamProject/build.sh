#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install

venv/bin/activate

python manage.py collectstatic --no-input

python manage.py migrate