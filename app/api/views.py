from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Quiz
from .task import quiz_api_update


class QuizAPIView(APIView):

    def get(self, request):
        data = {"response": "Запрос должен быть отправлен методом POST"}
        return Response(data, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        num = request.data.get("questions_num")
        if num:
            try:
                if num > 100 or num < 0:
                    data = {"response": "Количество вопросов должно быть от 0 до 100"}
                    return Response(data, status=status.HTTP_200_OK)
                quiz = Quiz.objects.last()
                quiz_api_update.delay(num)
                if quiz:
                    data = {
                        "question": quiz.question,
                        "answer": quiz.answer,
                    }
                    return Response(data, status=status.HTTP_200_OK)
                return Response(data=None, status=status.HTTP_200_OK)
            except TypeError:
                return Response({"response": "questions_num должен быть числом"},
                                status=status.HTTP_400_BAD_REQUEST)
        return Response(
            {"response": 'запрос должен быть с содержимым вида {"questions_num": integer}'},
            status=status.HTTP_400_BAD_REQUEST
        )

