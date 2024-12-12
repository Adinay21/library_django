# Generated by Django 5.1.4 on 2024-12-08 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/', verbose_name='загрузите фото книги')),
                ('title', models.CharField(max_length=100, verbose_name='напишите название книги')),
                ('description', models.TextField(blank=True, verbose_name='Напишите описание фильма')),
                ('price', models.FloatField(default=10, verbose_name='укажите цену книги')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('genre', models.CharField(choices=[('Ужасы', 'Ужасы'), ('Роман', 'Роман'), ('Приключения', 'Приключения')], default='Роман', max_length=100)),
                ('time_read', models.TimeField(blank=True, verbose_name='Укажите длительность аудиокниги')),
                ('author', models.CharField(default='А.С.Пушкин', max_length=100, verbose_name='Укажите автора книги')),
                ('audio_book', models.URLField(verbose_name='Укажите ссылку на аудиокнигу')),
            ],
        ),
    ]