# Generated by Django 5.1.4 on 2024-12-11 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_blog', '0002_alter_bookmodel_options_review'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
    ]
