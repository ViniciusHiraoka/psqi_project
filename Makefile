server:
	python3 manage.py runserver

migrations:
	python3 manage.py makemigrations && python3 manage.py migrate

shell:
	python3 manage.py shell