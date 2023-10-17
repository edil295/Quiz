# Quiz
1. Для запуска проекта необходимо создать внутри папки app/ файл entrypoint.sh с содержимым:
__________________________________________________________________________________________
'''
#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi


python manage.py migrate

exec "$@"
'''
_________________________________________________________________________________________
2. Далее, необходимо собрать докер машину, командой: <b>docker-compose up -d --build</b>
