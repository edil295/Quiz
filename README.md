Сервис для пополнения БД данными из сервиса https://jservice.io для Викторины

# Инструкция по установке проекта
1. Спулиться с ветки master:
2. Создать файл entrypoint.sh в директории app c содержимым:
__________________________________________________________________________________________
```
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
```
_________________________________________________________________________________________
2.1. Если операционная система Mac или Linux прописать команду в терминале:
   ```chmod +x entrypoint.sh```
   
3. Запустить сборку контейнеров командой: ```<b>docker-compose up -d --build</b>```
