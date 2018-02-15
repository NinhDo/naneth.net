swn:
	python manage.py makemigrations swn

migrate:
	python manage.py migrate

run:
	python manage.py runserver 0:8000

dbshell:
	python manage.py dbshell

.PHONY: swn migrate run dbshell source
