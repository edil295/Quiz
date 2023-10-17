import requests
from api.models import Quiz
from datetime import datetime


def objects_create(num, repetitions=1):
    """
    Создание объектов в БД,
    Функция является рекурсивной, т.е будет выполнятся до тех пор пока,
    она не получит уникальные объекты от API куда выполняется запрос.

                            Например: num=50
    Если из, 50 объектов полученных от API-запроса 10 уже существуют в нашей базе.
    Будет выполнен повторный запрос на получение 10 объектов, и так, до тех пор,
    пока мы не получим уникальные объекты

    :param num: количество объектов
    :param repetitions: глубина рекурсии, ограничен 100
    """
    if repetitions > 100:
        return
    if num > 0:
        count = 0
        response = requests.get(f"https://jservice.io/api/random?count={str(num)}")
        for r in response.json():
            formatted_datetime = datetime.strptime(r['created_at'], "%Y-%m-%dT%H:%M:%S.%fZ")
            data = {
                'id_quiz': r['id'],
                'answer': r['answer'],
                'question': r['question'],
                'created_at': formatted_datetime
            }
            try:
                if Quiz.objects.get(id=r['id']):
                    count += 1
            except Exception:
                Quiz.objects.create(
                    id_quiz=data['id_quiz'],
                    answer=data['answer'],
                    question=data['question'],
                    created_at=data['created_at']
                )
        objects_create(count, repetitions + 1)
