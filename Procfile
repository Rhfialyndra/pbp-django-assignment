release: sh -c 'python manage.py makemigrations && python manage.py migrate && python manage.py loaddata intial_catalog_data.json && python manage.py loaddata intial_mywatchlist_data.json'
web: gunicorn project_django.wsgi --log-file -
