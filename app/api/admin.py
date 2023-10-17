from django.contrib import admin

from .models import Quiz


class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_quiz', 'question', 'answer', 'created_at')


admin.site.register(Quiz, QuizAdmin)
