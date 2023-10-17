# Generated by Django 3.2 on 2023-10-17 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_quiz', models.BigIntegerField(editable=False)),
                ('question', models.TextField(verbose_name='Текст вопроса')),
                ('answer', models.TextField(verbose_name='Текст ответа')),
                ('created_at', models.DateTimeField(verbose_name='Дата создания вопроса')),
            ],
            options={
                'verbose_name': 'Викторина',
                'verbose_name_plural': 'Викторина',
                'ordering': ['created_at'],
            },
        ),
    ]
