# Generated by Django 5.1.4 on 2024-12-25 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='level',
            field=models.CharField(choices=[('jun', 'jun'), ('middle', 'middle'), ('senior', 'senior')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='salary',
            field=models.CharField(default='Зарплата не определена', max_length=50, null=True),
        ),
    ]
