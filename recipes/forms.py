from django import forms
from recipes.models import RecipeModel, IngredientModel, CollectionModel

class RecipeForm(forms.ModelForm):
    class Meta:
        model = RecipeModel
        fields = '__all__'


class IngredientForm(forms.ModelForm):
    class Meta:
        model = IngredientModel
        fields = '__all__'

class CollectionForm(forms.ModelForm):
    class Meta:
        model = CollectionModel
        fields = '__all__'