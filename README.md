Сервис для пополнения БД данными из сервиса https://jservice.io для Викторины

# Инструкция по установке проекта
1. Спулиться с ветки main:
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
```
   chmod +x entrypoint.sh
```
__________________________________________________________________________________________

3. Запустить сборку контейнеров командой: ```docker-compose up -d --build```
4. API-запрос должен быть отправлен POST-методом по данному URL -> **http://127.0.0.1:8000/api/v1/**
Тело запроса в формате JSON, {"questions_num": integer}, где integer -> это количество, вопросов с ответами который сервис должен получить из API **https://jservice.io**

<b>Пример JSON-тела</b>
~~~
   {"questions_num": 3}
~~~

5. Ответом на запрос будет предыдущей сохранённый вопрос-ответ для викторины. **https://jservice.io**. если такового не имеется(БД пустое), то мы получим пустое тело.

<b>Пример Response-овета</b>
~~~
{
    "question": "(Alex delivers the clue aboard a plane at the Aviano Air Base in Italy.) For over 30 years, the United States Air Force has relied on this fighter plane, a single             engine, Mach 2 F-16, known as \"The Fighting\" this; it's a fierce type of hawk",
    "answer": "\"Falcon\""
}
~~~
