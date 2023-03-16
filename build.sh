
# exit on error
set -o errexit

venv/bin/activate

python manage.py collectstatic --no-input

python manage.py migrate