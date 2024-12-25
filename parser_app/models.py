from django.db import models

class TopModel(models.Model):
    title = models.CharField(max_length=10000)
    image = models.URLField()
    description = models.CharField(max_length=10000)
    readers = models.CharField(max_length=100)

    def __str__(self):
        return self.title
