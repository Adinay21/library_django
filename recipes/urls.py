from django.urls import path
from . import views

urlpatterns = [
    path('recipe_list/', views.RecipeListView.as_view(), name='recipeList'),
    path('recipe_list/<int:id>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe_list/<int:id>/update/', views.UpdateRecipeView.as_view(), name='update_recipe'),
    path('recipe_list/<int:id>/delete/', views.DeleteRecipeView.as_view(), name='delete_recipe'),
    path('create_recipe/', views.CreateRecipeView.as_view(), name='create_recipe'),
    path('all_recipes/', views.AllRecipesView.as_view(), name='all_recipes'),
    path('soup_recipes/', views.SoupRecipesView.as_view(), name='soup_recipes'),
    path('meal_recipes/', views.MealRecipesView.as_view(), name='meal_recipes'),
    path('dessert_recipes/', views.DessertRecipesView.as_view(), name='dessert_recipes'),
]