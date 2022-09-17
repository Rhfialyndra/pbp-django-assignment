release: sh -c 'python manage.py makemigrations && python manage.py migrate && python manage.py loaddata *.json'
web: gunicorn project_django.wsgi --log-file -