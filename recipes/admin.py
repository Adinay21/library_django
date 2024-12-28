from django.contrib import admin
from recipes.models import RecipeModel, IngredientModel, CollectionModel

admin.site.register(RecipeModel)
admin.site.register(IngredientModel)
admin.site.register(CollectionModel)