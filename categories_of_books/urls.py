from django.urls import path
from . import views

urlpatterns = [
    path('all_books/', views.AllBooksView.as_view(), name='all_books'),
    path('books_for_kids/', views.BooksForKidsView.as_view(), name='books_for_kids'),
    path('books_for_teens/', views.BooksForTeensView.as_view(), name='books_for_teens'),
    path('books_for_youth/', views.BooksForYouthView.as_view(), name='books_for_youth'),
    path('books_for_pensioners/', views.BooksForPensionersView.as_view(), name='books_for_pensioners'),
]