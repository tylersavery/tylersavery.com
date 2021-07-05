.PHONY:  install run release web

install:
	npm install
	pip install -r requirements.txt

run:
	python manage.py runserver 0.0.0.0:8000

release:
	python manage.py migrate --noinput
	python manage.py compilemessages

web:
	gunicorn project.wsgi --log-file -