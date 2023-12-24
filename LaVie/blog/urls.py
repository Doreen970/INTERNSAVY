from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('articles/', views.article_list, name='article_list'),
    path('articles/<slug:slug>/', views.detail, name='detail'),
    path('create/', views.create_article, name='create_article'),
    path('dashboard/', views.dashboard, name='user_dashboard'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('edit/<slug:slug>/', views.edit, name='edit'),
    path('search/', views.search, name='search'),
]