install:
	pip install -r requirements.txt

test:
	cd ./source && python manage.py test

testuser:
	cd ./source && python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('root', 'fer.esp@gmail.com', 'password')"

dumpdata:
	cd ./source && \
	python manage.py dumpdata --indent 4 catv.Video > ./catv/fixtures/catv.Video.json && \
	python manage.py dumpdata --indent 4 catv.Playlist > ./catv/fixtures/catv.Playlist.json

loaddata:
	cd ./source && \
	python manage.py loaddata catv.Playlist.json && \
	python manage.py loaddata catv.Video.json
