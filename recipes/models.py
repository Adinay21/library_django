from django.db import models


class RecipeModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class IngredientModel(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=100)
    recipe = models.ForeignKey(RecipeModel, on_delete=models.CASCADE)
    is_optional = models.BooleanField(default=False, null=True, blank=True)
    calories = models.IntegerField(null=True, blank=True, verbose_name='укажите калорийность по желанию')
    notes = models.TextField(null=True, blank=True, verbose_name='укажите калорийность по желанию')


    def __str__(self):
        return self.name


class CollectionModel(models.Model):
    name = models.CharField(max_length=100)
    recipes = models.ManyToManyField(RecipeModel)

    def __str__(self):
        return self.name


