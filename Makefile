install:
	pip install -r requirements.txt

test:
    cd ./source && python manage.py test

dumpdata:
	cd ./source && python manage.py dumpdata --indent 4 catv.Video > ./catv/fixtures/catv.Video.json

loaddata:
	cd ./source && python manage.py loaddata catv.Video.json
