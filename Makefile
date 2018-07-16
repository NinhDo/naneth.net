swn:
	python manage.py makemigrations swn

migrate:
	python manage.py migrate

run:
	python manage.py runserver 0:8000

dbshell:
	python manage.py dbshell

static:
	python manage.py collectstatic --noinput -c

sass:
	python manage.py compilescss

test:
	coverage run manage.py test swn.tests api space

report:
	coverage report -m

.PHONY: swn migrate run dbshell static sass test report
