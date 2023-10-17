from django.db import models


class Quiz(models.Model):
    """
    Модель описывающая вопросы и ответы из викторины,
    данные заполняются с открытой API https://jservice.io/
    """
    id_quiz = models.BigIntegerField(
        editable=False
    )
    question = models.TextField(
        verbose_name='Текст вопроса'
    )
    answer = models.TextField(
        verbose_name='Текст ответа'
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания вопроса'
    )

    class Meta:
        verbose_name = 'Викторина'
        verbose_name_plural = 'Викторина'

    def __str__(self):
        return self.answer
