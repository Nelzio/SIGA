## Fazendo backup da base de dados
* python manage.py dumpdata --formar json --indent 4


* python manage.py dumpdata account home.Curso --format json --indent 4 > accountCursos.json

## Deleta todos migrations e cache do migrations

## Migrations e migrate

* python manage.py makemigrations
* python manage.py migrate

## load data que foi guardado

* python manage.py loaddata accountCursos.json 