from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<str:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<str:pk>/', views.delete_book, name='delete_book'),
    path('add_author/', views.add_author, name='add_author'),
    path('edit_author/<str:pk>/', views.edit_author, name='edit_author'),
    path('delete_author/<str:pk>/', views.delete_author, name='delete_author'),
]