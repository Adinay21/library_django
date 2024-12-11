from django.urls import path
from . import views

urlpatterns = [
    path('all_books/', views.all_books, name='all_books'),
    path('books_for_kids/', views.books_for_kids, name='books_for_kids'),
    path('books_for_teens/', views.books_for_teens, name='books_for_teens'),
    path('books_for_youth/', views.books_for_youth, name='books_for_youth'),
    path('books_for_pensioners/', views.books_for_pensioners, name='books_for_pensioners'),
]