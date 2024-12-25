from django.urls import path
from . import views

urlpatterns = [
    path('top_book_list/', views.TopListView.as_view(), name='top_list'),
    path('form_parser_top/', views.TopFormView.as_view()),
]