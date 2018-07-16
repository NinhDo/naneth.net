swn:
	python3 manage.py makemigrations swn

migrate:
	python3 manage.py migrate

run:
	python3 manage.py runserver 0:8000

dbshell:
	python3 manage.py dbshell

static:
	python3 manage.py collectstatic --noinput -c

sass:
	python3 manage.py compilescss

test:
	coverage run manage.py test swn.tests api space

report:
	coverage report -m

.PHONY: swn migrate run dbshell static sass test report
