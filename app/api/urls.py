from django.urls import path

from .views import QuizAPIView


urlpatterns = [
    path('v1/', QuizAPIView.as_view(), name='quiz'),
]
