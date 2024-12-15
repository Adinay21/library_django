from django.urls import path
from . import views

urlpatterns = [
    path('basket_list/', views.basket_list_view, name='basketList'),
    path('basket_list/<int:id>/', views.basket_detail_view, name='basket_detail'),
    path('basket_list/<int:id>/update/', views.update_basket_view, name='update_basket'),
    path('basket_list/<int:id>/delete/', views.delete_basket_view, name='delete_basket'),
    path('create_basket/', views.create_basket_view, name='create_basket'),
]