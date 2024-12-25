from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):
    CHOICES = (
        ('jun', 'jun'),
        ('middle', 'middle'),
        ('senior', 'senior')
    )
    level = models.CharField(max_length=100, null=True, choices=CHOICES)
    salary = models.CharField(max_length=50, default="Зарплата не определена", null=True)

    def save(self, *args, **kwargs):
        if self.level == 'jun':
            self.salary = "Зарплата 700$"
        elif self.level == 'middle':
            self.salary = "Зарплата 1000$"
        elif self.level == 'senior':
            self.salary = "Зарплата 2000$"
        else:
            self.salary = "Поднимите свой уровень"

        super().save(*args, **kwargs)