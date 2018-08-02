swn:
	python3 manage.py makemigrations swn

dnd:
	python3 manage.py makemigrations dnd

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
	coverage3 run manage.py test dnd.tests swn.tests api space

report:
	coverage3 report -m

.PHONY: swn migrate run dbshell static sass test report dnd
