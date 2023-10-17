from celery import shared_task
from .bussines_logic.update_quiz import objects_create

import requests


@shared_task
def quiz_api_update(num: int) -> None:
    """
    Обновление базы Quiz(Викторина) посредством POST-запроса в https://jservice.io/api/random?count=num.

    :param num: Количество вопросов в викторине.
    :return: None.
    """
    objects_create(num)
