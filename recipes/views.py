from django.shortcuts import render, get_object_or_404, redirect
from recipes.models import RecipeModel, IngredientModel, CollectionModel
from django.views import generic
from recipes.forms import IngredientForm, RecipeForm


class CreateRecipeView(generic.CreateView):
    template_name = 'recipe/create_recipe.html'
    form_class = RecipeForm
    success_url = '/recipe_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateRecipeView, self).form_valid(form=form)

class RecipeListView(generic.ListView):
    template_name = 'recipe/recipe_list.html'
    context_object_name = 'recipe_list'
    model = RecipeModel

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

class RecipeDetailView(generic.DetailView):
    template_name = 'recipe/recipe_detail.html'
    context_object_name = 'recipe_id'

    def get_object(self, **kwargs):
        recipe_id = self.kwargs.get('id')
        return get_object_or_404(RecipeModel, id=recipe_id)

class UpdateRecipeView(generic.UpdateView):
    template_name = 'recipe/recipe_update.html'
    form_class = RecipeForm
    success_url = '/recipe_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateRecipeView, self).form_valid(form=form)

    def get_object(self, **kwargs):
        recipe_id = self.kwargs.get('id')
        return get_object_or_404(RecipeModel, id=recipe_id)

class DeleteRecipeView(generic.DeleteView):
    template_name = 'recipe/confirm_delete.html'
    success_url = '/recipe_list/'

    def get_object(self, **kwargs):
        recipe_id = self.kwargs.get('id')
        return get_object_or_404(RecipeModel, id=recipe_id)


class IngredientDetailView(generic.DetailView):
    template_name = 'recipe/recipe_detail.html'
    context_object_name = 'ingredient_id'

    def get_object(self, **kwargs):
        ingredient_id = self.kwargs.get('id')
        return get_object_or_404(IngredientModel, id=ingredient_id)

class UpdateIngredientView(generic.UpdateView):
    template_name = 'recipe/recipe_update.html'
    form_class = IngredientForm
    success_url = '/recipe_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateIngredientView, self).form_valid(form=form)

    def get_object(self, **kwargs):
        ingredient_id = self.kwargs.get('id')
        return get_object_or_404(IngredientModel, id=ingredient_id)


class AllRecipesView(generic.ListView):
    template_name = 'recipe/all_recipes.html'
    context_object_name = 'recipes'
    model = CollectionModel

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

class SoupRecipesView(generic.ListView):
    template_name = 'recipe/soup_recipes.html'
    context_object_name = 'soup_recipes'
    model = CollectionModel

    def get_queryset(self):
        return self.model.objects.filter(tags__name='Супы').order_by('-id')


class MealRecipesView(generic.ListView):
    template_name = 'recipe/meal_recipes.html'
    context_object_name = 'meal_recipes'
    model = CollectionModel

    def get_queryset(self):
        return self.model.objects.filter(recipes__name='Вторые блюда').order_by('-id')


class DessertRecipesView(generic.ListView):
    template_name = 'recipe/dessert_recipes.html'
    context_object_name = 'dessert_recipes'
    model = CollectionModel

    def get_queryset(self):
        return self.model.objects.filter(recipes__name='Десерты').order_by('-id')

